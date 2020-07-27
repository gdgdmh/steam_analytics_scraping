#!/usr/bin/env python
"""エントリーポイント."""
import requests
from bs4 import BeautifulSoup
from sas import get_response
from sas import html_parse
from sas import scraping
from sas import ranking_data
from sas import sas_main
#  import re


def main():
    """エントリーポイント."""
    print('main')
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
    main = sas_main.SasMain()
    main.task()


if __name__ == '__main__':
    main()
