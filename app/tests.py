from django.test import TestCase

# Create your tests here.

import time,urllib2,json

t = str(time.time()).split('.')[0]
print t
url = 'http://m.toutiao.com/list/?tag=__all__&item_type=4&count=20&format=json&max_behot_time=%s' % t
req = urllib2.Request(url)
req.add_header('Content-type', 'application/json')
resp = urllib2.urlopen(req)
html= json.loads(resp.read())
print html['html']