# finish import part
import...



class main:

    def __init__(self):
        rospy.init_node('main',anonymous=False)
        #stop AIBot
	rospy.loginfo("To stop robot CTRL + c")
	#what function to call when you ctrol +c
	rospy.on_shutdown(self.shutdown)
        
        #image subscriber
        ......
        
        #command publisher      
        self.cmd_vel = rospy.Publisher('aibot/cmd_vel', Twist, queue_size=1) 
        self.move_cmd = Twist()  
        self.move_cmd.linear.x = 0.5
        self.move_cmd.angular.z = 0
    	
        
    def callback(self,data):
        ......
    
    def shutdown(self):
	#stop aibot
	rospy.loginfo("Stop robot")
	#a default twist has linear.x of 0 and angular.z of 0. So it will stop AIBot
	self.cmd_vel.publish(Twist())
	rospy.sleep(1)

if __name__ == '__main__':
    try:
        main()
        rospy.spin()
    except:
        rospy.loginfo("Lane Tracking node terminated.")
    


