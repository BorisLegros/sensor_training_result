#!/usr/bin/env python

import rospy
from sensor_msgs import PointCloud
from laser_assembler import AssembleScans

rospy.init_node('pubCloud')
pub = rospy.Publsher('~/cloud', PointCloud)
rate = rospy.Rate(5000)

while not rospy.is_shutdown():
	rospy.wait_for_service('assemble_scans')
	try:
		assScan = rospy.ServiceProxy('assemble_scans', AssembleScans)
		msg = PointCloud()
		msg = assemble_scans(0, 5000)
		pub.publish(msg)
	rate.sleep()