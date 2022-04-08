# ROS-Introduction-HelloTurtle

#### Start Hello Turtle Simulation in VC

Open the hello_turtle folder in VC and open the file called yTeleopKey.py

![Captura de pantalla de 2022-04-07 21-40-33](https://user-images.githubusercontent.com/64180738/162352524-a013dbb8-6875-49f4-92d5-6cf2d7b5cf9a.png)

Open a terminal in VC and type the following commands in catkin_ws folder to start the simulation


     source devel/setup.bash     
     roslaunch hello_turtle turtle.launch

A code was written that allows to operate a turtle from the turtlesim package with the keyboard, which complies with the following specifications:


• It must be moved forward and backward with the W and S keys

• You must turn clockwise and counterclockwise with keys D and A.

• You must return to your central position and orientation with the R key

• You must turn 180° with the SPACE key

For this, the necessary libraries were first imported


     import rospy
     from geometry_msgs.msg import Twist 
     from turtlesim.srv import TeleportAbsolute, TeleportRelative
     import termios, sys, os
     from turtlesim.srv import TeleportAbsolute 
     import argparse
     from numpy import pi

