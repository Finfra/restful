#!/usr/bin/env python
# http://www.dreamsyssoft.com/blog/blog.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html
import web
import xml.etree.ElementTree as ET

tree = ET.parse('./user-data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:        
    def GET(self):
        output = 'users:[';
        for child in root:
                    print ('child', child.tag, child.attrib)
                    output += str(child.attrib) + ','
        output += ']';
        return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
                return str(child.attrib)

if __name__ == "__main__":
    app.run()