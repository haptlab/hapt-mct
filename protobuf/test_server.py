#!/usr/bin/env python
# coding: utf-8

import cv2
from fpv_image_pb2 import *

import string,cgi,time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

WIDTH = 200 #80 #100
HEIGHT = 150 #60 #75
QUALITY = 40

cap = cv2.VideoCapture(0)

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            ret, frame = cap.read()
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (WIDTH, HEIGHT))
            #frame = cv2.resize(frame, (400, 300))

            # mirror
            frame = frame[:,::-1]

            cv2.imwrite("image.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), QUALITY])

	    fimage = FpvImage()
	    fimage.width = WIDTH
	    fimage.height = HEIGHT
	    fimage.image = open("image.jpg").read()
	    data = fimage.SerializeToString()

            self.send_response(200)
            self.send_header("Content-type", "binary/octet-stream")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
            return

        except IOError:
            self.send_error(404, "File Not Found: %s" % self.path)

if __name__ == "__main__":
    try:
        server = HTTPServer(('', 9999), MyHandler)
        print "started httpserver..."
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C received, shutting down server"
        cap.release()
        server.socket.close()

    #while True:
    #    ret, frame = cap.read()
    #    frame = cv2.resize(frame, (133, 100))
    #    frame = cv2.resize(frame, (400, 300))

    #    # mirror
    #    frame = frame[:,::-1]

    #    # show
    #    cv2.imshow("frame", frame)
    #    #cv2.imwrite("image.jpg", frame)

    #    k = cv2.waitKey(1)
    #    if k == 27: # press esc
    #        break

    #cap.release()
    #cv2.destroyAllWindows()

