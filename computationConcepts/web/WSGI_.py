# This is a demonstration of dynamic website creation with the "WSGIREF" module
#   WSGIREF is a reference implementation of the WSGI (Web Server Gateway Interface)
# specification that can be used to add WSGI support to a web server or framework. 
# It provides utilities for manipulating WSGI environment variables and response 
# headers, base classes for implementing SGI servers, a demo HTTP server that 
# serves WSGI applications, and a validation tool that checks WSGI servers and 
# applications for conformance to the WSGI specification (PEP 333).
#   This module is intended as a reference implementation of the specification,
# and as such shouldn't be used for general website development. 


# Simple serving of a string
"""
import wsgiref.simple_server

def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello n_n".encode("utf-8")]

server = wsgiref.simple_server.make_server('localhost', 8080, application)
server.serve_forever()
"""

# Simple serving of a file of content
import wsgiref.simple_server
def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/html")])

    fh = open("fileOfContent.content")
    lines = [fh.readline().encode("utf-8") for i in range(38)]

    return lines

server = wsgiref.simple_server.make_server('localhost', 8080, application)
server.serve_forever()