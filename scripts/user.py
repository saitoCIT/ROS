#! /usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

direction = ["Up","Down","Right","Left"]

print("0:Up 1:Down 2:Right 3:Left")
d = 0
NPC = direction[d]

if __name__ == '__main__':
    rospy.init_node('user')
    pub = rospy.Publisher('attimuite_hoi', Int32, queue_size = 1)
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        d = int(input(""))
        pub.publish(d)
        rate.sleep()
