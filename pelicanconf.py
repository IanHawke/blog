#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Hawke'
SITENAME = u'Ian Hawke'
SITEURL = 'http://ianhawke.github.io'
GITHUB_URL = 'https://github.com/IanHawke'
TWITTER_URL = 'https://twitter.com/IanHawke'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/IanHawke'),
          ('github', 'http://github.com/IanHawke'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='../pelican-themes/pelican-bootstrap3'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
ABOUT_ME = "Ian Hawke, numerical relativist, Southampton"
CC_LICENSE="CC-BY"
GITHUB_USER = "IanHawke"
TWITTER_USERNAME = "IanHawke"

# Statics paths mean than anything in these directories under content/*
# is copied into output/*.
# By default, this happens only for images. We need the notebook
# directory to be copied as well if we want to make the notebook
# source files available as part of the blog entries (which is
# generally a good idea).
STATIC_PATHS = ['images', 'notebooks']    # default setting is ['images']

# Sharing
TWITTER_USER = 'IanHawke'

# Tell pelican which directories contains the plugins
PLUGIN_PATHS = ["../pelican-plugins"]

# The next few lines allow automatic conversion of
# ipython notebooks to html as blog entries. We use Jake Vanderplaas'
# liquid_tags.notebook (see
# https://github.com/getpelican/pelican-plugins/blob/master/liquid_tags/Readme.md)

# Allow use of the following plugins:

PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook', 'series']

# the ipython notebook liquid_tags plugin needs the following:
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Define the directory below which notebooks (*.ipynb) need to be
# stored
NOTEBOOK_DIR = 'notebooks'

# Disqus
DISQUS_SITENAME = 'ianhawkeblog'
