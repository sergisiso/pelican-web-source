# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergi Siso'
SITENAME = u'Sergi Siso'
SITETITLE = u'Sergi Siso'
SITESUBTITLE = u'High Performance Software Engineer @ Hartree Centre'
DESCRIPTION = u'Sergi Siso Personal Webpage'
SITEURL = 'https://sergisiso.github.io'
THEME = 'Flex'
SITELOGO = SITEURL + '/images/prof2.jpg'
FAVICON = SITEURL + '/images/favicon.png'

CUSTOM_CSS = "custom.css"

EXTRA_PATH_METADATA = {
    "static/custom.css": {"path": "custom.css"},
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('', ''),)

# Social widget
SOCIAL = (('envelope', 'mailto:sergiesg@gmail.com'),
          ('github', 'https://github.com/sergisiso'),
          # ('bitbucket', 'https://bitbucket.org/ssiso'),
          ('instagram', 'https://www.instagram.com/sergisiso/'),
          ('twitter', 'https://twitter.com/sergiesg'),
          # ('facebook', 'https://www.facebook.com/sergi.siso.9'),
          ('linkedin', 'https://www.linkedin.com/in/sergisiso'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DISPLAY_RECENT_POSTS_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['static/custom.css', 'images', 'pdfs']

#PLUGIN_PATHS = [""]
#PLUGINS = [""]
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = "github"

COPYRIGHT_NAME = "Sergi Siso"
COPYRIGHT_YEAR = "2018-2020"
