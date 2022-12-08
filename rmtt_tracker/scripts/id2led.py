#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import Empty, String, UInt8

def callback(msg):
    pad_id = msg.data
    if pad_id == 1:
        # 在终端显示‘1‘
        rospy.loginfo('1')

if __name__ == "__main__":
    # 初始化ROS节点    
    rospy.init_node('pad_to_led', anonymous=False)
    # 定义订阅器和发布器
    # sub =
    # pub =
    rospy.spin()
        



