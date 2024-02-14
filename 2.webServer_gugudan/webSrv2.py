from http.server import HTTPServer, CGIHTTPRequestHandler
import os

# CGI 스크립트를 실행할 디렉토리 설정
os.chdir('.')

class Handler(CGIHTTPRequestHandler):
    # cgi-bin 디렉토리 내의 스크립트를 실행하기 위해 cgi_directories 설정
    cgi_directories = ['/cgi-bin']

PORT = 8002

httpd = HTTPServer(('', PORT), Handler)
print(f"Serving HTTP on port {PORT}...")
httpd.serve_forever()