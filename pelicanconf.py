#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#AUTHOR = u'SW'
SITENAME = u'Somatic Web'
SITEURL = 'http://somaticweb.org'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

LINKS =  (
#    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#    ('Python.org', 'http://python.org'),
#    ('Jinja2', 'http://jinja.pocoo.org'),
#    ('You can modify those links in your config file', '#'),
)

SOCIAL = (
    #('email', 'mailto:somaticweb@gmail.com'),
    ('identi.ca', 'http://identi.ca/somaticweb'),
    ('twitter', 'http://twitter.com/somaticweb'),
    ('reddit', 'http://www.reddit.com/user/somaticweb'),
    #('github', 'https://github.com/somaticweb'),
    #('gitorious', 'https://gitorious.org/~somaticweb'),
)

THEME = "swtheme"

DEFAULT_PAGINATION = 10

JINJA_EXTENSIONS = (
    'swjinja.myfilter',
)

USE_FOLDER_AS_CATEGORY = False

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

FILES_TO_COPY = (
    #('extra/robots.txt', 'robots.txt'),
)
