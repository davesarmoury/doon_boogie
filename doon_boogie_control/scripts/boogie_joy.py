#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

joy_init = False
joy_msg = None

def callback(msg):
    joy_msg = msg
    joy_init = True

def boogie():
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

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(min_rate)

    while not rospy.is_shutdown():
        if joy_init:
            now = rospy.get_time()

            if now - joy_msg.header.stamp < max_df * 2.0:
                cmd_msg = Twist()

                vel = ( joy_msg.axes[pedal_index] - pedal_min ) / (pedal_max - pedal_min)
                vel = max(0.0, min(1.0, vel))
                vel = vel * max_vel

                yaw = joy_msg.axes[wheel_index]
                yaw = max(0.0, min(1.0, yaw)) * 2.0 - 1.0
                yaw = yaw * max_yaw

                pub.publish(cmd_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        boogie()
    except rospy.ROSInterruptException:
        pass
