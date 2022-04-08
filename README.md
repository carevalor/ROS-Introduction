# ROS-Introduction-HelloTurtle

#### Start Hello Turtle Simulation in VC

Open the hello_turtle folder in VC and open the file called myTeleopKey.py

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

```python
import rospy
from geometry_msgs.msg import Twist 
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from turtlesim.srv import TeleportAbsolute 
import argparse
from numpy import pi
```
     
To detect if a key was pressed, a function called "getkey" was added. Which was taken from the code available at this link: http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html.


If a key is pressed, it must detect which key was pressed. For this, the function called "check" was created.
```python     
def check(key): 
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
```
An aditional key 'q' was created to finish the process. 

Movements with the A, S, D, and W keys were achieved through the turtle1/cmd vel topic, while movements with the R and SPACE keys were achieved through the services turtle1/teleport absolute and turtle1/teleport relative.
        
        
![Captura de pantalla de 2022-04-07 21-34-15](https://user-images.githubusercontent.com/64180738/162356140-5f4c0633-ea08-4384-a55b-707f6fe47043.png)

      
Note that both, teleport and rel_teleport functions uses services, while pubVel is a publisher to the cmd_vel topic. 
