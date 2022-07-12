# Steps for Jupiter Robot Arm Movements

For the robot to operate, we will have to open up 4 terminals:

| Step  | Terminal # | Description                                                | Command                                                            |
| :---: | :--------: | ---------------------------------------------------------- | ------------------------------------------------------------------ |
|   1   |     1      | Bring up the Jupiter robot arm                             | roslaunch jupiterobot_arm_bringup joints_bringup.launch            |
|   2   |     2      | Bring up the turtlebot                                     | roslaunch turtlebot_bringup minimal.launch                         |
|   3   |     3      | Activate Turtlebot teleoperation with keyboard             | roslaunch turtlebot_teleop keyboard_teleop.launch                  |
|   4   |     4      | Open the hand (2.0 will open the hand to the widest: 10cm) | rostopic pub -1 /hand_controller/command std_msgs/Float64 -- 2.0   |
|   5   |     4      | Put down the elbow                                         | rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- 0.0  |
|   6   |     4      | Close the hand to grip the rubbish                         | rostopic pub -1 /hand_controller/command std_msgs/Float64 -- -1.0  |
|   7   |     4      | Back to the initial position                               | rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- -1.5 |
|   8   |     3      | Locating the rubbish bin using turtlebot rotating function | `j` (rotate left) or `l` (rotate right)                            |
|   9   |     4      | Put down the elbow                                         | rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- 0.0  |
|  10   |     4      | Open the hand to drop the rubbish                          | rostopic pub -1 /hand_controller/command std_msgs/Float64 -- 2.0   |
|  11   |     4      | Back to the initial position                               | rostopic pub -1 /elbow_controller/command std_msgs/Float64 -- -1.5 |
|  12   |     4      | Close the hand                                             | rostopic pub -1 /hand_controller/command std_msgs/Float64 -- -1.0  |

