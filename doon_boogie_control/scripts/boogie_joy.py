#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node('doon_boogie', anonymous=True)

    wheel_index = rospy.get_param("~wheel/index")
    wheel_min = rospy.get_param("~wheel/min")
    wheel_max = rospy.get_param("~wheel/max")
    pedal_index = rospy.get_param("~pedal/index")
    pedal_min = rospy.get_param("~pedal/min")
    pedal_max = rospy.get_param("~pedal/max")

    max_vel = rospy.get_param("~max_vel")
    max_yaw = rospy.get_param("~max_yaw")
    min_rate = rospy.get_param("~min_rate")
    max_dv = 1.0 / min_rate

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
