#!/usr/bin/python
import time
import os

for num in range(0,23):
  os.system('clear')
  print "   Happy Birthday!"
  print "                     "
  if num > 10:
    print "   Make a Wish..."
  else:
    print ""
  if num > 13:
    print "   Start counting ... "
  else:
    print ""
  if num > 15:
    print "        3"
  else:
    print ""
  if num > 17:
    print "        2 "
  else:
    print ""
  if num > 19:
    print "        1 "
  else:
    print ""
  if num < 21:
    print ""
    if num%2 == 0: 
      print "    *    *     *  "
    else:
      print "     *    *     *  "
  else:
    print ""
    print ""
  print "     ||   ||    ||  "
  print "  (===============)"
  print "  ( ************* )"
  print "  (_______________)"
  print ""
 
  time.sleep(1)