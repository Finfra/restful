#!/usr/bin/env python
import web
import random

urls = (
    '/getString', 'getString',
)

app = web.application(urls, globals())

class getString:        
    def GET(self):
        r=random.random()
        return r

if __name__ == "__main__":
    app.run()
