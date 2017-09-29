
Pelican (pyhthon) static web page generator for sergisiso.github.com

Instructions
---------------
Install pelican and python-bs4

Edit files under 'content' folder

Execute 'pelican content' to generate webpage under 'output'

Preview the result with 'cd output' and 'python -m pelican.server'

Add modifications to the static site repository with 'rsync -avc --exclude=.git --delete output/ ../sergisiso.github.com/'

Push the changes on this repo and the static site repo.

Pelican documentation[http://docs.getpelican.com/en/stable/index.html]
