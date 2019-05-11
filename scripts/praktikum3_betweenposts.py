#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from robotont_sensors.msg import LaserScanSplit

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)


distances = LaserScanSplit()


def scan_callback(data):
    global distances
    distances = data

#def minDist():
#            if (distances.centerMin < 0.4) OR (distances.rightMin < 0.4) OR (distances.leftMin < 0.4):
#                vel_msg.linear.x = -vel_msg.linear.x
#            elseif (vel_msg.linear.x < 0):
#                vel_msg.linear.x = -vel_msg.linear.x
#            else:
#                pass



def turn45Right():
    for i in range(0,1):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = 1.5
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def turn45Left():
    for i in range(0,1):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = -1.5
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def move():
    global distances
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    rospy.Subscriber('/scan_to_distance', LaserScanSplit, scan_callback)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################

        if distances.centerMin > 0.6:
            vel_msg.angular.z = 0
            vel_msg.linear.x = 0.3
        #    minDist()
        elif (distances.rightMin < distances.leftMin):
            vel_msg.linear.x = 0
            vel_msg.angular.z = 1
        elif (distances.rightMin > distances.leftMin):
            vel_msg.linear.x = 0
            vel_msg.angular.z = -1
        else:
            vel_msg.linear.x = -0.3

        ######################
        # YOUR CODE HERE END #
        ######################
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.05)


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
