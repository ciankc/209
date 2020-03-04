#!/bin/bash

# create backup copy
cp lee_position_controller_node.cpp.o lee_position_controller_node.cpp.o.orig

truncate -s +4 lee_position_controller_node.cpp.o

# get expected CRC value
CRC=$(gdb -x gdbscript firmware_updater.o | grep "Calculated" | cut -d ":" -f2)

# update object file to have CRC
./addcrc lee_position_controller_node.cpp.o $CRC
mv lee_position_controller_node.cpp.o.crc lee_position_controller_node.cpp.o
cp lee_position_controller_node.cpp.o ~/catkin_ws/build/rotors_control/CMakeFiles/lee_position_controller_node.dir/src/nodes/lee_position_controller_node.cpp.o
