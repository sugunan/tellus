from http.server import BaseHTTPRequestHandler, HTTPServer
import simplejson
import os
import logging
import configparser
import util_func as uf

config = configparser.RawConfigParser()
config.read("app.properties")
conf_log_path = config.get("LogSection", "log.path")
conf_log_level = config.get("LogSection", "log.level")
logging.basicConfig(filename=conf_log_path,
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s',
                    level=int(conf_log_level))


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):

        # this will take current path as web directory, If different path to be given then update it
        serve_from = os.getcwd()
        logging.info('Current web directory: %s ', serve_from)

        path = serve_from + self.path
        
        if self.path == "/":
            path = serve_from + "/index.html"

        path_list = uf.get_path_list()
        if self.path in path_list:
            self.send_response(200)
            self.end_headers()
            uf.uri_func(self)
        elif not os.path.abspath(path).startswith(serve_from):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Private!")
        elif os.path.isdir(path):
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(os.listdir(path)).encode())
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Directory not found")
        else:
            try:
                with open(path, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
            # error handling skipped
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        logging.info('Post method invoked')
        self.data_string = self.rfile.read(int(self.headers["Content-Length"]))

        data = simplejson.loads(self.data_string)

        serve_from = os.getcwd()
        logging.info('Current web directory: %s ', serve_from)

        path = serve_from + self.path

        path_list = uf.get_path_list()
        if self.path in path_list:
            self.send_response(200)
            self.end_headers()
            uf.uri_func(self)
        elif not os.path.abspath(path).startswith(serve_from):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Private!")
        elif os.path.isdir(path):
            try:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(os.listdir(path)).encode())
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Directory not found")
        else:
            try:
                with open(path, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data)
            # error handling skipped
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")
        return


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
