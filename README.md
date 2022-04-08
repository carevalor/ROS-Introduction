# ROS-Introduction-HelloTurtle

#### Start Hello Turtle Simulation in VC

Open the hello_turtle folder in VC and open the file called yTeleopKey.py

![Captura de pantalla de 2022-04-07 21-40-33](https://user-images.githubusercontent.com/64180738/162352524-a013dbb8-6875-49f4-92d5-6cf2d7b5cf9a.png)

Open a terminal in VC and type the following commands to start the simulation


                    source devel/setup.bash
          
                    roslaunch hello_turtle turtle.launch


First launch three linux terminals. At the first terminal run the following commnand to start ROS.

`$ roscore`

Then, run the following command to start the hello turtle simulation

`$ rosrun turtlesim turtlesim_node`
