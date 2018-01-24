#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import time
import os

local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com'
con = requests.get(url)
bHave = False

#soup = BeautifulSoup(con.content, "html.parser")
#print(soup.prettify(encoding="utf-8"))
reg = '(?<={url: ").+?.jpg(?=")'
pattren = re.compile(reg)
tag = re.search(pattren, con.text)
if tag:
    urlEnd = tag.group()
    if urlEnd:
        url = url + urlEnd
        global bHave
        bHave = True

    if bHave:
        print(url)
        read = requests.get(url)
        sPath = __file__
        sPath = os.path.dirname(sPath)
        sPath = sPath + '/Pic'
        if not os.path.exists(sPath):
            os.makedirs(sPath)

        picName = "%s/%s.jpg" % (sPath, local)
        with open(picName, 'wb') as f:
            f.write(read.content)
