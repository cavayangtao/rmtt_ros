#!/usr/bin/env python3

import rospy
import tf2_ros
from tf.transformations import quaternion_from_euler, euler_from_quaternion
import turtlesim.msg
from geometry_msgs.msg import TransformStamped

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()

    t = TransformStamped()
    # Read message content and assign it to
    # corresponding tf variables
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = turtlename
    
    # Turtle only exists in 2D, thus we get x and y translation
    # coordinates from the message and set the z coordinate to 0
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0

    # For the same reason, turtle can only rotate around one axis
    # and this why we set rotation in x and y to 0 and obtain
    # rotation in z axis from the message
    q = quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('turtle1_tf2_broadcaster')
    turtlename = 'turtle1'
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
