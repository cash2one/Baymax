# coding=utf-8
__author__ = 'guguohai@outlook.com'

import re,urllib2

def getBingImg(url):
    re_img = re.compile(r'(?<=g_img=\{url:\').*?(?=.jpg)')
    html = urllib2.urlopen(url).read()

    match = re_img.search(html)
    if match:
        return match.group() + '.jpg'