#! /bin/bash
WD=$(pwd)
cp ./lee_position_controller_node.cpp ~/catkin_ws/src/CrazyS/rotors_control/src/nodes/lee_position_controller_node.cpp
rm ~/catkin_ws/build/rotors_control/CMakeFiles/lee_position_controller_node.dir/src/nodes/lee_position_controller_node.cpp.o 
cd ~/catkin_ws
catkin build
cd ~/Assignment2Files
cp ~/catkin_ws/build/rotors_control/CMakeFiles/lee_position_controller_node.dir/src/nodes/lee_position_controller_node.cpp.o .
# added signature when generating binary
cd $WD
gpg --output firmware.sig --detach-sig ~/catkin_ws/build/rotors_control/CMakeFiles/lee_position_controller_node.dir/src/nodes/lee_position_controller_node.cpp.o

