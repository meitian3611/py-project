import streamlit as st
import os
from openai import OpenAI
import html
from datetime import datetime
import json


# 保存会话信息
def save_session_data():
    if st.session_state.current_session:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        os.makedirs("sessions", exist_ok=True)
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


# 生成会话名称
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


# 获取会话的json数据
def get_session_data():
    session_list = []
    if os.path.exists("sessions"):
        for file in os.listdir("sessions"):
            if file.endswith(".json"):
                session_list.append(file.replace(".json", ""))
    session_list.sort(reverse=True)
    return session_list


# 加载会话信息 显示在主聊天框中
def load_session_data(session_name):
    try:
        if session_name and os.path.exists(f"sessions/{session_name}.json"):
            # 存在数据 加载打开会话信息
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.messages = session_data["messages"]
                st.session_state.current_session = session_name
            st.rerun()
    except Exception:
        st.error("加载会话失败")


# 删除会话
def delete_session(session_name):
    try:
        if session_name and os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            if session_name == st.session_state.current_session:
                st.session_state.current_session = generate_session_name()
                st.session_state.messages = []
            st.rerun()
    except Exception:
        st.error("删除会话失败")


# 设置页面的配置项
st.set_page_config(
    page_title="AI智能聊天",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
)
# 大标题
st.title("AI智能聊天")

# 初始化信息
if "messages" not in st.session_state:
    st.session_state.messages = []

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "mm"

if "nature" not in st.session_state:
    st.session_state.nature = "高冷又魅惑的南方女孩,喜欢称呼用户为哥哥"

if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 左侧侧边栏信息
with st.sidebar:
    st.subheader("AI控制面板")
    # 新建会话的按钮
    if st.button("新建会话", width="stretch", icon="✏️"):
        save_session_data()
        if st.session_state.messages:
            st.session_state.current_session = generate_session_name()
            st.session_state.messages = []
            save_session_data()
            st.rerun()

    st.text("会话列表")
    session_info = get_session_data()
    for session in session_info:
        col1, col2 = st.columns([4, 1])
        # 加载会话
        with col1:
            if st.button(session, key=f"load_{session}", width="stretch", icon="📒",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                load_session_data(session)
        # 删除会话
        with col2:
            if st.button("", key=f"del_{session}", width="stretch", icon="🗑️"):
                delete_session(session)

    st.divider()

    st.subheader("定制特征")

    nick_name = st.text_input("昵称: ", placeholder="请输入昵称...", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格: ", placeholder="请输入性格...", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

st.text(f"会话名称: {st.session_state.current_session}")
# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(html.escape(message["content"]))

# 系统角色提示词
system_prompt = f"""
    你叫 %s,你是一个美少女甜妹。现在是用户的真实伴侣,请完全代入角色
    规则:
        1.每次只回复1句话
        2.匹配用户的语言
        3.和微信聊天一样,简短一些
        4.符合伴侣性格方式的对话
        5.内容要充分体现出伴侣的性格特征
        6.禁止任何场景或状态描述文字
    伴侣性格:
         %s
    你必须遵守上诉规则来回复用户
"""
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    # 显示用户输入的文本
    st.chat_message("user").write(html.escape(prompt))
    # 缓存用户输入的文本
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 AI 大模型
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # print(f"传递给AI的参数是: {st.session_state.messages}")

    # 显示 AI 输出的文本(非流式输出)
    # st.chat_message("assistant").write(html.escape(response.choices[0].message.content))

    # 显示 AI 输入的文本(流式输出)
    response_message = st.empty()  # 创建一个空的消息框, 用于显示流式输出
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += html.escape(content)
            response_message.chat_message("assistant").write(html.escape(full_response))

    # 缓存 AI 输出的文本
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
    st.session_state.messages.append({"role": "assistant", "content": full_response})  # 流式

    # 保存会话信息
    save_session_data()
