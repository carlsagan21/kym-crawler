# -*- coding: utf-8 -*-

from crawler import *


category_list = [
    'kimym_books',
    'kimym_movies',
    'kimym_scrap',
    'kimym_data',
    'kimym_etc',
    'kimym_dayone',
    'kimym_notice'
]

crawl(get_category_limit(category_list))
