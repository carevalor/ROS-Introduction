from cgi import print_environ
from tkinter import W
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
from pynput.keyboard import Key, Listener, Controller

TERMIOS= termios
keyboard = Controller()

def on_press(key):
    if key == Key.space:
        pubVel(0,1,2.2)
    #if key == keyboard.press('w'):
        #pubVel(0,1,2.2)
    
def on_release(key):
    if key == Key.esc:
        return False

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def check(tecla):
    if (tecla==b'w'):
        pubVel(1,0,1)
    if (tecla==b's'):
        pubVel(-1,0,1)
        

if __name__ == '__main__':
    while(1):
        pubVel(0,0,0.1)
        tecla=getkey();
        print(tecla)
        check(tecla);

    