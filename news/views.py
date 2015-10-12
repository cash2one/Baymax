# coding=utf-8

from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import time, urllib2, re, json, httplib
import xml.sax
import xml.sax.handler

class XMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping



def cnbeta(request):
    try:
        url = 'http://rss.cnbeta.com/rss'
        req = urllib2.Request(url)
        req.add_header('Content-Type','application/rss+xml')
        response = urllib2.urlopen(req)
        xh = XMLHandler()
        xml.sax.parseString(response.read(), xh)
        ret = xh.getDict()
        return render_to_response("news/news.html", ret, context_instance=RequestContext(request))
    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print u"连接失败,错误原因", e.reason
            return None

def csdn(request):
    try:
        url = 'http://www.csdn.net/article/rss_lastnews'
        req = urllib2.Request(url)
        req.add_header('Content-Type','application/rss+xml')
        response = urllib2.urlopen(req)
        xh = XMLHandler()
        xml.sax.parseString(response.read(), xh)
        ret = xh.getDict()
        return render_to_response("news/news.html", ret, context_instance=RequestContext(request))
    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print u"连接失败,错误原因", e.reason
            return None


def wap(request):
    return render_to_response("news/wap_bak.html", {"testcase": ''}, context_instance=RequestContext(request))


def wap_con(request):
    return render_to_response("news/wap_content.html", {"testcase": ''}, context_instance=RequestContext(request))


def wap_menu(request):
    return render_to_response("news/wap_menu.html", {"testcase": ''}, context_instance=RequestContext(request))


# def result_data(request):
# page = request.GET.get('page')
#     response_data = []
#
#     temp_data = [{'result': 'Facebook本周举行开发者大会', 'image': 'http://p2.pstatp.com/list/2575/443537243'},
#                  {'result': '迪斯尼CEO曾隐瞒乔布斯病情长达三年之久', 'image': 'http://p1.pstatp.com/list/2575/540112485'},
#                  {'result': '网络租房比例过半 94%网民怨中介费高', 'image': 'http://p2.pstatp.com/list/2563/3821559120'},
#                  {'result': '披着“羊皮”朋友圈谣言 你还能明辨吗', 'image': 'http://p2.pstatp.com/list/2551/405337174'},
#                  {'result': '网友免费在线听歌，环球等唱片公司', 'image': 'http://p1.pstatp.com/list/2540/6698892493'}]
#
#     for i in range(0, 5):
#         response_data.append(temp_data)
#
#     response_data.append(None)
#
#     return HttpResponse(json.dumps(response_data[int(page)]), content_type="application/json")

def wap_new(request):
    return render_to_response("news/wap.html", {"testcase": ''}, context_instance=RequestContext(request))


def wap_result(request):
    t = str(time.time()).split('.')[0]

    url = 'http://m.toutiao.com/list/?tag=__all__&item_type=4&count=20&format=json&max_behot_time=%s' % t
    req = urllib2.Request(url)
    req.add_header('Content-type', 'application/json')
    try:
        resp = urllib2.urlopen(req)
        html = resp.read()
    except httplib.IncompleteRead:
        return HttpResponse('')

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

    return HttpResponse(new_html)