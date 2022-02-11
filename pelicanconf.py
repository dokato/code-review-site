#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'DK'
SITENAME = 'Code Review Workshop '
SITEURL = ''
SITESUBTITLE = '(for researchers)'
SITEDATE = '10 Feb 2022'
PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
   ('Software Sustainability Institute', 'https://www.software.ac.uk/'),
   ('Article: Code Review For and By Scientists', 'https://arxiv.org/pdf/1407.5648.pdf'),
   ('Constructive Code Critique', 'https://www.software.ac.uk/blog/2017-05-11-constructive-code-critique'),
   ('Turing Way Book: Code Review Chapter', 'https://the-turing-way.netlify.app/reproducible-research/reviewing.html'),
   ('Code of Conduct', 'https://www.software.ac.uk/programmes-and-events/code-conduct')
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGE_TITLE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/bricks2/"
