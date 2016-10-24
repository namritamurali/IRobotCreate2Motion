#!/usr/bin/env python3

'''
robotest.py - Test the features of BreezyCreate2

This code is part of BreezyCreate2

The MIT License

Copyright (c) 2016 Simon D. Levy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

from breezycreate2 import Robot
import time
import sys

def init_bot():
    bot = Robot()
    time.sleep(1)
    
    return bot

# given a distance in mm, have the robot move at intervals of this distance
def control_dist(bot, dist):
    move_time = float(dist) / 20
    print "move time is {}".format(move_time)
    #while 1:
    start_time = time.time()
    print "starting dist = {} mm".format(bot.read_distance())
    while (abs(start_time - time.time()) < move_time):
        bot.setForwardSpeed(20)
    dist = bot.read_distance()
    print "distance traveled = {} mm".format(dist)
    # pause for 3 seconds ?
    bot.setForwardSpeed(0)
    time.sleep(3)
def reset(bot):
    bot.stop()
    bot.close()

def wait_for_read(mins):
    time.sleep(mins*60)

def IRdetect(bot, vel):
    bot.read_distance()
    prev_l = prev_r = 0
    while 1:
        (l, r) = bot.getIRSensors()
        #print (l, r)
        (lv, rv) = bot.getLRVelocity()
        print (lv, rv)
        if ((l >= 2000 or r >= 2000) and not(prev_l >= 2000 or prev_r >= 2000)):
            bot.setForwardSpeed(0)
            dist = bot.read_distance()
            print "distance traveled = {} mm".format(dist)
            #wait_for_read(1)
            time.sleep(3)
        (prev_l, prev_r) = (l,r)
        bot.setForwardSpeed(vel)

def main(bot, vel, secs=60):
    while 1:
        start_time = time.time()
        while (start_time - time.time() < secs):
            bot.setForwardSpeed(vel)


if __name__ == "__main__":
    try:
        bot = init_bot()
        #control_dist(bot, int(sys.argv[1]))
        #print bot.getirsensors()
        if len(sys.argv) > 2:
            main(bot, int(sys.argv[1]), int(sys.argv[2]))
        else:
            main(bot, int(sys.argv[1]))
    except KeyboardInterrupt:
        bot.setForwardSpeed(0)
        bot.stop()
        bot.close()
        print "Robot connection closed. Exiting...\n\n"
        sys.exit(0)
