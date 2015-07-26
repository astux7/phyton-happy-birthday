#!/usr/bin/python
import time
import os

class Cake:
  'Class of the cake'
   
  def displayCake(self):
    print "   ||   ||    ||   "
    print "(=================)"
    print "( *************** )"
    print "(_________________)"

class Candles:
  'Class of the candles'
   
  def flame(self, num):
    if num < 21:
      if num%2 == 0: 
        print "  *    *     *  "
      else:
        print "   *    *     *  "
    else:
      print ""

class BirthdayText:
  "Birthday text"

  def birthdayMessage(self):
    print "   Happy Birthday!"
    print ""

  def wishMessage(self, num):
    if num > 10:
      print "   Make a Wish..."
    else:
      print ""

  def countingMessage(self, num):
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

text = BirthdayText()

for num in range(0,23):

  os.system('clear')

  text.birthdayMessage()

  text.wishMessage(num)
  
  text.countingMessage(num)

  Candles().flame(num)

  Cake().displayCake()

  print ""

  time.sleep(1)
