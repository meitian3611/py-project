import pandas as pd
import matplotlib.pyplot as plt
import os

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据文件路径（相对于本文件所在目录）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'movies_list.csv')
SAVE_PATH = os.path.join(BASE_DIR, 'data', 'movies_list.png')


def load_data() -> pd.DataFrame:
    """读取并加载电影数据"""
    data = pd.read_csv(CSV_PATH, usecols=[
        '电影名称', '上映年份', '上映时间', '电影标签', '播放时长', '评分', '语言'
    ], dtype={
        '上映年份': 'Int64',
    })
    return data


def plot_yearly_movie_count(ax: plt.Axes, data: pd.DataFrame):
    """统计每年电影数量的折线图"""
    year_counts = data.groupby('上映年份')['上映年份'].count()
    min_year = year_counts.index.min()
    max_year = year_counts.index.max()
    x = [i for i in range(min_year, max_year + 1)]
    y = [year_counts.get(i, 0) for i in x]

    ax.plot(x, y, linewidth=2, color='green')
    ax.set_title('每年电影数量变化', fontsize=16, fontweight='bold')
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.set_xticks(x[::10])
    ax.set_yticks([i for i in range(0, 12, 1)])
    ax.grid(True, linestyle='--', alpha=0.3)


def plot_language_bar_chart(ax: plt.Axes, data: pd.DataFrame):
    """统计不同语言的电影数量柱状图"""
    data_lang = data.groupby('语言')['语言'].count().sort_values(ascending=False)
    x_lang = data_lang.index
    y_lang = data_lang.values

    ax.bar(x_lang, y_lang, width=0.5, color='green')
    ax.set_title('不同语言电影数量', fontsize=16, fontweight='bold')
    ax.set_xlabel('语言', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.set_xticks(x_lang)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='x', rotation=90)


def plot_genre_bar_chart(ax: plt.Axes, data: pd.DataFrame):
    """统计不同标签的电影数量柱状图"""
    type_count = {}
    for tags in data['电影标签'].str.split(','):
        for tag in tags:
            type_count[tag] = type_count.get(tag, 0) + 1

    x_types = list(type_count.keys())
    y_types = list(type_count.values())

    ax.bar(x_types, y_types, width=0.5, color='green')
    ax.set_title('不同类型电影数量', fontsize=16, fontweight='bold')
    ax.set_xlabel('类型', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.set_xticks(x_types)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.tick_params(axis='x', rotation=90)


def plot_score_pie_chart(ax: plt.Axes, data: pd.DataFrame):
    """统计各个评分的电影占比饼状图"""
    score_count = data.groupby('评分')['评分'].count()
    total_scores = score_count.sum()
    large_scores = score_count.loc[score_count >= total_scores * 0.05]
    small_scores = score_count.loc[score_count < total_scores * 0.05]

    if small_scores.sum() > 0:
        large_scores['其他'] = small_scores.sum()

    ax.pie(large_scores, labels=large_scores.index, autopct='%1.1f%%', startangle=90, radius=1.2)
    ax.set_title('电影评分占比', fontsize=16, fontweight='bold', y=1.05)
    ax.legend(bbox_to_anchor=(-0.2, -0.3), loc='lower left', fontsize=12, title='评分', ncol=4)


def main():
    """主函数：加载数据、创建图表、保存并展示"""
    pd.set_option('display.min_rows', 20)

    # 读取数据
    data = load_data()

    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    fig.suptitle('电影榜单数据可视化统计', fontsize=20)
    fig.subplots_adjust(hspace=0.8)

    ax1: plt.Axes = axes[0, 0]
    ax2: plt.Axes = axes[0, 1]
    ax3: plt.Axes = axes[1, 0]
    ax4: plt.Axes = axes[1, 1]

    # 绘制四个图表
    plot_yearly_movie_count(ax1, data)
    plot_language_bar_chart(ax2, data)
    plot_genre_bar_chart(ax3, data)
    plot_score_pie_chart(ax4, data)

    # 保存图片并显示
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    plt.savefig(SAVE_PATH)
    plt.show()


if __name__ == '__main__':
    main()
