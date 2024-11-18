from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1 align="center">ASIN RENIX 24900126</h1>
           <ol>
               <li>Device name	Asin</li>
              <li>Processor	12th Gen Intel(R) Core(TM) i5-1235U   1.30 GHz</li>
              <li>Installed RAM	16.0 GB (15.7 GB usable)</li>
              <li>Device ID	BA9DD6A3-F5F9-4F25-92CB-52F0970DB865</li>
              <li>Product ID	00342-42670-33810-AAOEM</li>
              <li>System type	64-bit operating system, x64-based processor</li>
              <li>Pen and touch	No pen or touch input is available for this display</li>
          </u1>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()