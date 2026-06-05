import csv
import requests
from lxml import html
import re

MOVIES_LIST_FILE = "resources/movie_list.csv"
TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


# 保存数据
def save_all_movies(all_movies):
    if not all_movies:
        print("没有数据可保存")
        return
    with open(MOVIES_LIST_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_movies[0].keys())
        writer.writeheader()  # 写入表头
        writer.writerows(all_movies)  # 写入数据
        print(f"成功保存 {len(all_movies)} 条电影数据")


# 获取电影详情数据
def get_movie_info(movie_info_url):
    movie_response = requests.get(movie_info_url, timeout=30)
    print(f"发送请求: {movie_info_url} 获取电影详情的数据...")
    movie_doc = html.fromstring(movie_response.text)
    # 获取数据信息  地址需要根据网站结构灵活变动调整
    movie_name = movie_doc.xpath("//section[@class='header poster']/div[1]/h2/a/text()")  # 电影名称
    movie_years = movie_doc.xpath("//section[@class='header poster']/div[1]/h2/span/text()")  # 上映年份
    movie_dates = movie_doc.xpath("//span[@class='release']/text()")  # 上映时间
    movie_tags = movie_doc.xpath('//span[@class="genres"]/a/text()')  # 电影标签
    movie_times = movie_doc.xpath('//span[@class="runtime"]/text()')  # 播放时长
    movie_scores = movie_doc.xpath('//div[@class="user_score_chart"]/@data-percent')  # 评分
    movie_languages = movie_doc.xpath('//section[@class="facts left_column"]/p[last()-2]/text()')  # 语言
    movie_directors = movie_doc.xpath('//div[@class="header_info"]/ol/li[1]/p[1]/a/text()')  # 导演
    movie_authors = movie_doc.xpath('//div[@class="header_info"]/ol/li[2]/p[1]/a/text()')  # 作者
    movie_actors = movie_doc.xpath('//*[@id="cast_scroller"]/ol/li/p[1]/a/text()')  # 主演
    movie_slogans = movie_doc.xpath('//h3[@class="tagline"]/text()')  # 宣传语
    movie_des = movie_doc.xpath('//div[@class="overview"]/p/text()')  # 描述

    # 返回一个字典格式
    movie_info = {
        "电影名称": movie_name[0].strip() if movie_name else '',
        "上映年份": get_movie_years(movie_years),
        "上映时间": get_movie_dates(movie_dates),
        "电影标签": ",".join(movie_tags) if movie_tags else '',
        "播放时长": get_movie_times(movie_times),
        "评分": movie_scores[0].strip() if movie_scores else '',
        "语言": movie_languages[0].strip() if movie_languages else '',
        "导演": ",".join(movie_directors) if movie_directors else '',
        "作者": ",".join(movie_authors) if movie_authors else '',
        "主演": ",".join(movie_actors) if movie_actors else '',
        "宣传语": movie_slogans[0].strip() if movie_slogans else '',
        "描述": movie_des[0].strip() if movie_des else '',
    }
    return movie_info


# 进行数据格式化处理
def get_movie_years(movie_years):
    movie_year = movie_years[0].strip() if movie_years else ''
    return movie_year.replace("(", "").replace(")", "")  # 去掉括号


def get_movie_dates(movie_dates):
    movie_date = movie_dates[0].strip() if movie_dates else ''
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", movie_date)
    if not m:
        m = re.search(r"(\d{2})/(\d{2})/(\d{4})", movie_date)
        return f"{m.group(3)}-{m.group(1)}-{m.group(2)}" if m else movie_date
    return m.group()


def get_movie_times(movie_times):
    # 播放时长 2h 30m 转换为 150m
    movie_time = movie_times[0].strip() if movie_times else ''
    h_res = re.search(r"(\d+)h", movie_time)
    m_res = re.search(r"(\d+)m", movie_time)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return f"{h * 60 + m}m"


# 主函数, 核心逻辑
def main():
    all_movies = []  # 保存所有电影信息

    for page_num in range(1, 2):  # 1-5页
        # 1.发送请求
        response = requests.get(TMDB_TOP_URL + f"?page={page_num}", timeout=30)
        print("发送请求 获取电影榜单的数据...")

        # 2.解析数据
        document = html.fromstring(response.text)
        movies_list = document.xpath('//div[contains(@class, "comp:poster-card")]')
        print(f"开始获取第 {page_num} 页的数据...", )

        # 3.遍历信息
        for movie in movies_list:
            movie_urls = movie.xpath("./div/div/a/@href")
            if movie_urls:
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 发送请求 获取详情数据
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 4.保存数据
    print("数据获取完成, 保存数据到 CSV 文件中...")
    save_all_movies(all_movies)


if __name__ == '__main__':
    main()
