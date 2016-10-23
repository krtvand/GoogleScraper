#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError

keywords = ['site:*.rossvyaz.ru -www.rossvyaz.ru']

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    'keywords': keywords,
    #'keyword_file': '../gov_req.txt',
    'search_engines': 'google',
    'num_pages_for_keyword': 2,
    'scrape_method': 'selenium',
    'sel_browser': 'chrome',
    'print_results': 'summarize',
    'clean_cache_files': False
}

search = scrape_with_config(config)