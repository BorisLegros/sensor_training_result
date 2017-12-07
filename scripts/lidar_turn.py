#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node('lidar_turn')
pub = rospy.Publisher('/laser_velocity_controller/command', Float64)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	msg = Float64()
	msg = 1.0
	pub.publish(msg)
	rate.sleep()