#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num
import actionlib, time
from control_msgs.msg import FollowJointTrajectoryAction
from std_srvs.srv import SetBool, SetBoolResponse

def talker():
    # while not rospy.is_shutdown():    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    pub = rospy.Publisher('chatter', Num, queue_size=10)
    Mymsg=Num()
    rospy.wait_for_service('/gripper/run')
    Gripper_Client = rospy.ServiceProxy('/gripper/run', SetBool)

    # Mymsg.num=[-0.37,0.03,0,0,0,90,0] # Initial
    Mymsg.num=[-0.37,0.15,0,0,0,90,0] # Suck
    print('Go to',Mymsg.num)
    start_time=time.time()
    end_time=time.time()
    while(end_time-start_time <12):
        pub.publish(Mymsg)
        rate.sleep()
        end_time=time.time()
    
    print('Open gripper:')
    Gripper_Client(1)
    time.sleep(2)

    Mymsg.num=[-0.37,-0.15,0.05,0,0,90,0] # Start
    print('Go to',Mymsg.num)
    start_time=time.time()
    end_time=time.time()
    while(end_time-start_time <10):
        pub.publish(Mymsg)
        rate.sleep()
        end_time=time.time()

    Mymsg.num=[-0.2,-0.15,0.05,0,0,0,0] # End
    print('Go to',Mymsg.num)
    start_time=time.time()
    end_time=time.time()
    while(end_time-start_time <15):
        pub.publish(Mymsg)
        rate.sleep()
        end_time=time.time()

    Mymsg.num=[-0.2,0.12,0.05,0,0,0,0] # Push
    print('Go to',Mymsg.num)
    start_time=time.time()
    end_time=time.time()
    while(end_time-start_time <10):
        pub.publish(Mymsg)
        rate.sleep()
        end_time=time.time()

    print('Close gripper:')
    Gripper_Client(0)
    time.sleep(2)
    print('Bye-Bye')


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
