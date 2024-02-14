#!/usr/bin/env python
# http://www.dreamsyssoft.com/blog/blog.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html
import web

urls = (
    '/getString', 'getString',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class getString:        
    def GET(self):
        output = '{"x":1,"y":2}'
        return output

class get_user:
    def GET(self, user):
        return user

if __name__ == "__main__":
    app.run()
