#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#AUTHOR = u'SW'
SITENAME = u'Somatic Web'
SITEURL = 'http://somaticweb.org'

FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = 'feeds/all.atom.xml'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

LINKS =  (
    ("userops mailing list", "http://lists.mediagoblin.org/listinfo/userops"),
    ("Sandstorm", "https://sandstorm.io/"),
)

SOCIAL = (
    ('email', 'mailto:somaticweb@gmail.com'),
    ('twitter', 'https://twitter.com/somaticweb'),
    #('googleplus', 'https://plus.google.com/u/0/111187535762987664866'),
    ('reddit', 'http://www.reddit.com/user/somaticweb'),
    ('github', 'https://github.com/somaticweb'),
)

TWITTER_USERNAME = "somaticweb"

THEME = "swtheme"

DEFAULT_PAGINATION = 10

JINJA_EXTENSIONS = (
    'swjinja.myfilter',
)

USE_FOLDER_AS_CATEGORY = False

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# https://github.com/getpelican/pelican/blob/master/docs/settings.rst#path-metadata
STATIC_PATHS = (
    'extra/robots.txt',
    'extra/humans.txt',
)
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
}
