#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'Cooper Stimson'
SITENAME = 'stimson.io'
SITEURL = ''
CURRENTYEAR = str(datetime.date.today().year)
GITHUB_URL = 'https://github.com/6c1/stimson.io'

PATH = 'content'
THEME = './theme'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('twitter', 'cooperstimson'),
    ('github', '6c1'),
    ('linkedin', 'cooperstimson/'),
    ('lastfm', 'mdccxxix'),
    ('goodreads', '8570098-cooper'),
)
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = False

ARTICLE_PATHS = ['articles']
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
INDEX_SAVE_AS = '/blog/index.html'

MENUITEMS = (
    ('Blog', '/blog'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ["/Users/cooperstimson/pelican-plugins"]
PLUGINS = [
    'tag_cloud',
]
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True
