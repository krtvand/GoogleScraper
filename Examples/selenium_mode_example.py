#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from GoogleScraper import scrape_with_config, GoogleSearchError
from GoogleScraper import database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

keywords = ['site:*.altsovet.ru -www.altsovet.ru']

# See in the config.cfg file for possible values
config = {
    'use_own_ip': False,
    #'keywords': keywords,
    'keyword_file': '../gov_req.txt',
    'search_engines': 'google',
    'num_pages_for_keyword': 5,
    'scrape_method': 'selenium',
    'sel_browser': 'chrome',
    #'clean_cache_files': True,
    'proxy_file' : 'proxy',
    'check_proxies': False,
    'output_filename': 'log',
    'print_results': 'summarize'

}

proxies = ['http 194.54.64.90:5093', 'http 194.54.64.90:5094',
           'http 194.54.64.90:5095', 'http 194.54.64.90:5096',
           'http 194.54.64.90:5097']

with open('proxy', 'w') as f:
    f.write(random.choice(proxies))

search = scrape_with_config(config)
def write_to_file():
    engine = create_engine('sqlite:///' + 'google_scraper.db')

    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    ds = set()
    for q in s.query(database.Link).all():
        ds.add(q.domain)

    print(len(ds))

    with open('gov_sd', 'w') as f:
        for d in ds:
            f.write(d + '\n')

