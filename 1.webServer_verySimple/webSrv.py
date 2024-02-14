from http.server import HTTPServer, SimpleHTTPRequestHandler
#import os
#os.chdir("/xxx")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8001)  # 빈 문자열은 모든 인터페이스에서 접속 허용을 의미합니다.
    httpd = server_class(server_address, handler_class)
    print("Serving HTTP on port 8001...")
    httpd.serve_forever()

run()