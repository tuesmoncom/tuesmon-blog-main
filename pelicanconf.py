#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEBUG=1

AUTHOR = 'Tuesmon'
AUTHOR_EMAIL = 'support@tuesmon.com'
SITENAME = 'Tuesmon Blog'
SITEURL = 'https://blog.tuesmon.com'
SITESUBTITLE = 'Tuesmon is a project management platform for startups and agile developers & designers'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('Tuesmon.com', 'https://tuesmon.com'),
         ('Mailing list', 'https://groups.google.com/forum/#!forum/tuesmoncom'),
         ('Kaleidos', 'http://www.kaleidos.net/'),
         ('ΠWEEK', 'http://piweek.com/'),
)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/tuesmoncom'),
          ('Github', 'https://github.com/tuesmoncom'),
          ('Google+', 'https://plus.google.com/+TuesmonIo'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Extra files to copy
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/humans.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

#settings for Pelican
DEFAULT_CATEGORY = 'General'
THEME = 'theme/tuesmon'
DISQUS_SITENAME = "tuesmon-blog"

#Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gravatar', 'sitemap', 'open_graph']


PRIVACY_POLICY_URL = "http://tuesmon.com/privacy-policy"

SITEMAP = {
    "format": "xml",
    "priorities": {
        "home": 1.0,
        "articles": 0.8,
        "indexes": 0.5,
        "authors": 0.6,
    }
}
