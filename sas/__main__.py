#!/usr/bin/env python
"""エントリーポイント."""
import requests
from bs4 import BeautifulSoup
from sas import get_response
from sas import html_parse
from sas import scraping
from sas import ranking_data
#  import re


def main():
    """エントリーポイント."""
    print('main')
    url = "https://store.steampowered.com/stats/?l=japanese"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    print(type(html))
    print(type(soup))
    #  print(soup)
    # DOMの階層メモ
    # body class v6 responsive_page
    #  responsive_page_content
    #    responsive_page_template_content
    #      page_content
    #        topgames_col
    #          detailStats
    #            player_count_row
    #              currentServers
    #              gameLink

    # 各ゲームの[現在のプレイヤー数と本日のピーク数]を取得する(100個まで取得できるのでlist化)
    elem_cs = soup.find_all(class_="currentServers")
    player_counts = []
    count = int(len(elem_cs) / 2)
    for i in range(count):
        game_counts = []
        game_counts.append(elem_cs[i * 2].text)
        game_counts.append(elem_cs[(i * 2) + 1].text)
        player_counts.append(game_counts)
    print(player_counts)
    # 各ゲームのタイトル名を取得する
    game_names = []
    elem_gl = soup.find_all(class_="gameLink")
    cnt = int(len(elem_gl))
    for i in range(cnt):
        game_names.append(elem_gl[i].text)
    # print(game_names)

    # test
    r = get_response.GetResponse("https://store.steampowered.com/stats/?l=japanese")
    r.request()
    res = r.get()
    s = html_parse.HtmlParse(res)
    s.parse()
    soup = s.get()
    sc = scraping.Scraping(soup)
    sc.scraping()


if __name__ == '__main__':
    main()
