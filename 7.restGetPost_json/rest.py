#!/usr/bin/env python
# http://www.dreamsyssoft.com/blog/blog.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html
import web
import random
import time, datetime
import json
import urllib.parse


urls = (
    '/get', 'getString',
    '/post', 'getString'
)

app = web.application(urls, globals())

class getString:        
    def GET(self):
        r=random.random()
        now = time.localtime()
        nows = time.strftime("%Y-%m-%d %H:%M:%S", now)
        output = '{"time":"%s","y":%f}'%(nows,r)
        return output
    def POST(self):
        str1=web.data()
        dic1 = urllib.parse.parse_qs(str1.decode() )
        return json.dumps(dic1)

if __name__ == "__main__":
    app.run()
