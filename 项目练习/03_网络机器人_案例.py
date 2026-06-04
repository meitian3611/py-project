import requests
import csv
from lxml import html

TMDB_BASE_URL = "https://www.themoviedb.org/"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"


# 主函数,核心逻辑
def main():
    # 1.发送请求
    response = requests.get(TMDB_TOP_URL, timeout=30)

    # 2.解析数据
    document = html.fromstring(response.text)
    movies_list = document.xpath("//*[@id='page_1']/div/div/div")

    # 3.遍历信息
    all_movies = []
    for movie in movies_list:
        movie_urls = movie.xpath("./div/div/a/@href")
        if movie_urls:
            movie_info_url = TMDB_TOP_URL + movie_urls[0]
            # 发送请求 获取详情数据
            # movie_info = get_movie_info(movie_info_url)
            # all_movies.append(movie_info)

    # 4.保存数据


if __name__ == '__main__':
    main()
