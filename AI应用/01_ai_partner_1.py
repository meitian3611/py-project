import streamlit as st
import os
from openai import OpenAI
import html

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
)
# 初始化信息
if "messages" not in st.session_state:
    st.session_state.messages = []

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "mm"

if "nature" not in st.session_state:
    st.session_state.nature = "高冷又魅惑的南方女孩,喜欢称呼用户为哥哥"

# 大标题
st.title("AI智能伴侣")

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

# 左侧侧边栏信息
with st.sidebar:
    st.subheader("伴侣信息")

    nick_name = st.text_input("昵称: ", placeholder="请输入昵称...", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格: ", placeholder="请输入性格...", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(html.escape(message["content"]))

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
    print(f"传递给AI的参数是: {st.session_state.messages}")

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
