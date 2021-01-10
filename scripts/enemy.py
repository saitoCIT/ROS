#! /usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

attimuite_hoi = ["Up","Down","Right","Left"]

enemy = random.randint(0,3)
user = 0

def cb(message):
    global user
    global enemy
    enemy = random.randint(0,3)
    user = message.data
    print("enemy turn to the %s" % (attimuite_hoi[enemy]))
    if user == enemy:
        rospy.loginfo('You Win')
    else :
        rospy.loginfo('You Lose')

if __name__ == '__main__':
    rospy.init_node('enemy')
    sub = rospy.Subscriber('attimuite_hoi', Int32, cb)
    pub = rospy.Publisher('result', Int32, queue_size = 1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rate.sleep()
