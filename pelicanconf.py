# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergi Siso'
SITENAME = u'Sergi Siso'
SITEURL = ''
THEME = 'pelican-twitch-modified'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('', ''),)

# Social widget
SOCIAL = (('EMAIL', 'mailto:sergiesg@gmail.com'),
        ('Github','https://github.com/sergisiso'),
        ('Bitbucket','https://bitbucket.org/ssiso'),
        ('Linkedin', 'https://www.linkedin.com/in/sergisiso'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'pdfs']

PLUGIN_PATHS = ["plugins/pelican-toc"]
PLUGINS = ["toc"]
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = "github"
