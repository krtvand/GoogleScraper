#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError

keywords = ['site:*.altsovet.ru -www.altsovet.ru']

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    #'keywords': keywords,
    'keyword_file': '../gov_req.txt',
    'search_engines': 'google',
    'num_pages_for_keyword': 5,
    'scrape_method': 'http',
    'sel_browser': 'firefox',
    #'clean_cache_files': True,
    #'proxy_file' : 'proxy',
    'check_proxies': False,
    'print_results': 'summarize'

}

search = scrape_with_config(config)