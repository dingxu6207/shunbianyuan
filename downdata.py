# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:41:53 2019

@author: dingxu
"""

import urllib.request
import re
import os

# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.fts)'
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('gb2312'))
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


root_url = 'http://psp.china-vo.org/pspdata/2019/05/20190531/15~16%2050~70/'

#raw_url = 'http://psp.china-vo.org/pspdata/2019/06/20190603/13~14%2050~60/'
raw_url = root_url

html = getHtml(raw_url)
url_lst = getUrl(html)

#os.mkdir('E:/ldf_download')
os.chdir(os.path.join(os.getcwd(), 'ldf_download'))

for url in url_lst[:]:
    url = root_url + url
    getFile(url)

