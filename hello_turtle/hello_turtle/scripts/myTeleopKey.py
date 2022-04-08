import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
from turtlesim.srv import TeleportAbsolute


def pubVel(vel_x, ang_z, t): #Publicador de velocidad en el tópico cmd_ve
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def teleport(x, y, ang): #Teletransporte para volver a posición de InicioT
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def rel_tp(x, ang): #Función de Teletranspe Relativo para Giro de 180°
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportR(x,ang)
        print('Teleported to x: {}, ang: {}'.format(str(x),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

TERMIOS= termios 
def getkey(): #Detectar la Letra
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
    
def check(key): #Revisar que tecla fue pesionada
    if (key==b'w'):
        pubVel(1,0,1)
    if (key==b's'):
        pubVel(-1,0,1)
    if (key==b'a'):
        pubVel(0,1,1)
    if (key==b'd'):
        pubVel(0,-1,1)
    if (key==b' '):
        rel_tp(0, pi)
    if (key==b'r'):
        teleport(5, 5, 0)
    if (key==b'q'):
        exit()


if __name__ == '__main__':
    while(1):
        try:
            pubVel(0,0,0.1)
            key=getkey(); # Guarda la tecla presionada
            check(key); #Revisa que tecla fue presionada para operar
        except rospy.ROSInterruptException:
            pass