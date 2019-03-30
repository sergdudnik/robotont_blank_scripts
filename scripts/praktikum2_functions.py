#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

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

#######################
# YOUR FUNCTIONS HERE #
#######################
def ruutforward(rto,xspeed): 
    for i in range(0,rto): # 30 
        vel_msg.linear.x = xspeed # 0.2
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def forward(howlong,withwhichspeed):
    if withwhichspeed < 0: 
        withwhichspeed = -withwhichspeed 
    for i in range(0,howlong): # 30 
        vel_msg.linear.x = withwhichspeed
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def backward(howlong,withwhichspeed): 
    if withwhichspeed > 0:
         withwhichspeed = -withwhichspeed 
    for i in range(0,howlong): # 30 
        vel_msg.linear.x = withwhichspeed
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)



def turnleft(howlong,withwhichspeed): 
    if withwhichspeed < 0:
         withwhichspeed = -withwhichspeed
    for i in range(0,howlong): # 30 
        vel_msg.linear.x = 0 
        vel_msg.linear.y = 0
        vel_msg.angular.z = withwhichspeed
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def turnright(howlong,withwhichspeed): 
    if withwhichspeed > 0:
         withwhichspeed = -withwhichspeed
    for i in range(0,howlong): # 30 
        vel_msg.linear.x = 0 
        vel_msg.linear.y = 0  
        vel_msg.angular.z = withwhichspeed
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)



def ruutturn(rto,zspeed):
    for i in range(0,rto):  # 30
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = zspeed # 0.6
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def ruut():
    side = 0
    while side < 4:
        ruutforward(30,0.2)
        ruutturn(30,0.6)
        side += 1


###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

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
        # vel_msg.linear.x = 0
        # vel_msg.linear.y = 0
        # vel_msg.angular.z = 0
        # velocity_publisher.publish(vel_msg)
        # rospy.sleep(0.1)

        forward(50,0.2)

        # turnleft(30,0.2)

        # backward(50,0.2)

        turnright(30,0.2)

        ruut()        

        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
