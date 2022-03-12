# -*- coding utf-8 -*-
import requests
import re

url = 'http://whdownload.com/games.php?name=%&sort=0&dir=0'

home_url = "http://whdownload.com/"

pattern = re.compile(r'<td><a\shref="(.+?)">', re.S)

r = requests.get(url)

links = re.findall(pattern, r.text)

for link in links:
    print "Downloading: %s" % link
    r = requests.get("%s%s" % (home_url, link))
    f = open(link.split('/')[-1], 'wb')
    f.write(r.content)
    f.close()
