#!/usr/bin/env python3

import rospy
import rospkg
import std_msgs.msg
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

# resize the image to w*h
w = 360
h = 240

def callback(msg):

    img = bridge.imgmsg_to_cv2(msg)
    img = cv2.resize(img, (w, h))    
    cv2.imshow('Frame', img)
    cv2.waitKey(1)

if __name__ == '__main__':

    rp = rospkg.RosPack()
    path = rp.get_path("rmtt_tracker")
    bridge = CvBridge()
    rospy.init_node('face_tracker', anonymous=True)
    sub = rospy.Subscriber("image_raw", Image, callback)
    rospy.spin()