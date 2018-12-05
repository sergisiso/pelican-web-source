# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergi Siso'
SITENAME = u'Sergi Siso'
SITETITLE = u'Sergi Siso'
SITESUBTITLE = u'High Performance Software Engineer @ Hartree Centre'
DESCRIPTION = u'Sergi Siso Personal Webpage'
SITEURaL = ''#'http://www.sergisiso.com'
THEME = 'flex-theme'
#SITELOGO = SITEURL + '/images/profile.png'
#FAVICON = SITEURL + '/images/favicon.ico'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('', ''),)

# Social widget
SOCIAL = (('email', 'mailto:sergiesg@gmail.com'),
        ('github','https://github.com/sergisiso'),
        ('bitbucket','https://bitbucket.org/ssiso'),
        ('linkedin', 'https://www.linkedin.com/in/sergisiso'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_RECENT_POSTS_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'pdfs']

#PLUGIN_PATHS = [""]
#PLUGINS = [""]
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = "github"
