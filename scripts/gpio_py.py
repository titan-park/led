#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import String

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

dt = 0
dtMax = 1024
dtMin = 0

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

	if data.data == 'a' :
		print "Left"
		GPIO.output(23, True)
		GPIO.output(24, False)
	elif data.data == 'w':
		print "Forward"
		GPIO.output(23, True)
		GPIO.output(24, True)
	elif data.data == 'd':
		print "Right"
		GPIO.output(23, False)
		GPIO.output(24, True)
	elif data.data == 's':
		print "Stop"
		GPIO.output(23, False)
		GPIO.output(24, False)

def gpio_py():
	rospy.init_node('gpio_py', anonymous=True)

	rospy.Subscriber("Num", String, callback)


	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	gpio_py()
