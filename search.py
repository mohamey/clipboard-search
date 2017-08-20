#!/usr/bin/python

import pyperclip
import subprocess
import os

clipboard = pyperclip.paste().strip()
search_string = clipboard.replace(' ', '+')

search_query = "http://www.google.com/search?q={query}".format(query=search_string)

FNULL = open(os.devnull, 'w')
subprocess.call(['/usr/bin/xdg-open', search_query], stdout=FNULL, stderr=subprocess.STDOUT)
