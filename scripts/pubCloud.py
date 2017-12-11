#!/usr/bin/env python

import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *
from sensor_msgs.msg import PointCloud
from laser_assembler import AssembleScans
rospy.init_node('pubCloud')
pub = rospy.Publisher('~/cloud', PointCloud, queue_size=10)
rate = rospy.Rate(5000)
msg = AssembleScans()

while not rospy.is_shutdown():
	rospy.wait_for_service('assemble_scans')
	assemble_scans = rospy.ServiceProxy('assemble_scans', AssembleScans)
	msg = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
	pub.publish(msg)
	rate.sleep()