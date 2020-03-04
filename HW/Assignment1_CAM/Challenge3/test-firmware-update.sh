#! /bin/bash
# new firmware software update
./firmware_updater.o firmware.sig ~/catkin_ws/build/rotors_control/CMakeFiles/lee_position_controller_node.dir/src/nodes/lee_position_controller_node.cpp.o 
if [ $? -eq 0 ]; then
    echo "OK"
    roslaunch rotors_gazebo mav_with_waypoint_publisher.launch
else
    echo "Resetting environment..."
    cp lee_position_controller_node.cpp.save ~/catkin_ws/src/rotors_control/src/nodes/lee_position_controller_node.cpp
    cd ~/catkin_ws
    catkin build
    cd ~/Assignment2 Files
fi

