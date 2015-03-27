# coding=utf-8
from django.test import TestCase

# Create your tests here.

import time, urllib2, json, re,httplib

def aaa():
    t = str(time.time()).split('.')[0]

    url = 'http://m.toutiao.com/list/?tag=__all__&item_type=4&count=20&format=json&max_behot_time=%s' % t
    req = urllib2.Request(url)
    req.add_header('Content-type', 'application/json')
    try:
        resp = urllib2.urlopen(req)
        html = resp.read()
    except httplib.IncompleteRead:
        return ''

    html_len = len(html)
    e = 0
    sections = []
    while e < html_len:
        sec_dict = {}
        s = e + html.find('<section')
        e = e + html.find('</section>')

        section = html[s:e]
        # print section+'\n\n'

        line3 = '<h3'
        h3_start = section.find(line3)
        h3_end = section.find('</h3>')

        sec_dict['h3'] = section[h3_start:h3_end].replace(line3, '')

        imgs = re.findall(r'<img src=\\"([^\"]+)\\"', section)
        sec_dict['img'] = imgs

        sections.append(sec_dict)

    new_html = ''
    href = '<a href="/news/wap_con/" class="clearfix">'
    tips = '<div class="comment-tips"><div class="time-action"><time>40分钟前</time><button class="fa fa-heart-o" onclick="showFav(this);return false"></button></div><span>网易新闻</span><i class="fa fa-comment-o"></i><b>488</b></div>'
    tips1 = '<div class="comment-tips"><span>网易新闻</span><i class="fa fa-comment-o"></i><b>488</b></div>'
    tips2 = '<div class="time-action"><time>40分钟前</time><button class="fa fa-heart-o" onclick="showFav(this);return false"></button></div>'
    for s in sections:
        h3 = '<h3>' + s['h3'].replace('class=\\"line3\\" >', '') + '</h3>'
        h3 = h3.decode('unicode_escape')
        h3 = h3.encode('utf-8')

        imgs = s['img']

        if len(imgs) > 2:
            img_str = '<ul class="img-list clearfix">'
            for img in imgs:
                img_str += '<li><div class="img-wrap"><img src="%s" /></div></li>' % img
            img_str += '</ul>'
            sec = '<section>%s%s%s</a>%s</section>' % (href, h3, img_str, tips)
        elif len(imgs) > 0:
            sec = '<section>%s<img src="%s" class="imgr" />%s%s</a>%s</section>' % (
                href, imgs[0], h3, tips1, tips2)
        else:
            sec = '<section>%s%s</a>%s</section>' % (href, h3, tips)

        new_html += sec
    return new_html

if __name__ == "__main__":
    print aaa()