#!/usr/bin/env python3
# -*-coding:utf-8-*-
# Copyright (c) 2023 Tao: yangtao@nwpu.edu.cn.

# ROS
import rospy
from rmtt_core18 import tt_driver

if __name__ == '__main__':
    robomaster_node_name = rospy.get_name()
    robomaster_node_namespace = rospy.get_namespace()
    rospy.loginfo('Node with namespace = {}, name = {} started'.format(
    robomaster_node_namespace, robomaster_node_name))
    rospy.loginfo('Running until shutdown (Ctrl-C).')
    # Initialize ROS node
    rospy.init_node('tt_driver_node', anonymous=False)
    try:
        driver = tt_driver()
    except rospy.ROSInterruptException:
        pass