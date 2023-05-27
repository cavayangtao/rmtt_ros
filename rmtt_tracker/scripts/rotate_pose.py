#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import numpy as np

def callback(msg):
    # Extract the current pose information from the message
    x = msg.pose.position.x
    y = msg.pose.position.y
    z = msg.pose.position.z
    roll, pitch, yaw = euler_from_quaternion([msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w])
    
    # Rotate the pose by 180 degrees around y axis
    yaw += np.deg2rad(180)
    qx, qy, qz, qw = quaternion_from_euler(roll, pitch, yaw)

    # Create a new PoseStamped message with the rotated position and orientation
    new_msg = PoseStamped()
    new_msg.header = msg.header
    new_msg.pose.position.x = x
    new_msg.pose.position.y = y
    new_msg.pose.position.z = z
    new_msg.pose.orientation.x = qx
    new_msg.pose.orientation.y = qy
    new_msg.pose.orientation.z = qz
    new_msg.pose.orientation.w = qw

    # Publish the new PoseStamped message
    pub.publish(new_msg)

rospy.init_node('rotate_pose_node')
sub = rospy.Subscriber('/pose', PoseStamped, callback)
pub = rospy.Publisher('/new_pose', PoseStamped, queue_size=10)
rospy.spin()
