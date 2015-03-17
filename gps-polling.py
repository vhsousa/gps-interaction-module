__author__ = 'vhsousa'
#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
import time

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

if __name__ == '__main__':
    gpsd = gps(host="10.3.1.240", port=8080, mode=WATCH_ENABLE) #starting the stream of info

    while True:
        try:
              #It may take a second or two to get good data

              gpsd.next()
              print gpsd
              print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
              #os.system('clear')

              # print
              # print ' GPS reading'
              # print '----------------------------------------'
              # print 'latitude    ' , gpsd.fix.latitude
              # print 'longitude   ' , gpsd.fix.longitude
              # print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
              # print 'altitude (m)' , gpsd.fix.altitude
              # print 'eps         ' , gpsd.fix.eps
              # print 'epx         ' , gpsd.fix.epx
              # print 'epv         ' , gpsd.fix.epv
              # print 'ept         ' , gpsd.fix.ept
              # print 'speed (m/s) ' , gpsd.fix.speed
              # print 'climb       ' , gpsd.fix.climb
              # print 'track       ' , gpsd.fix.track
              # print 'mode        ' , gpsd.fix.mode
              # print
              # print 'sats        ' , gpsd.satellites

              time.sleep(1) #set to whatever

        except Exception, e:
            print e
            continue
