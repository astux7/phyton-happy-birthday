#!/usr/bin/python
import time
import os

 
def displayCake():
  print "   ||   ||    ||   "
  print "(=================)"
  print "( *************** )"
  print "(_________________)"


def flame(num):
  if num < 21:
    if num%2 == 0: 
      print "  *    *     *  "
    else:
      print "   *    *     *  "
  else:
    print ""

def birthdayMessage():
  print "   Happy Birthday!"
  print ""

def wishMessage(num):
  if num > 10:
    print "   Make a Wish..."
  else:
    print ""

def countingMessage(num):
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


for num in range(0,23):

  os.system('clear')

  birthdayMessage()

  wishMessage(num)
  
  countingMessage(num)

  flame(num)

  displayCake()

  print ""

  time.sleep(1)
