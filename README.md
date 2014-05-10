MNSU3DModelingKit
=================

For use with the MNSU, Mankato Archeology Department 3D modeling project

## cam.py
main python file to be ran in Linux envoirment
Depends on GPIO ACM0 being open and arudino writing to it.
This GPIO is written to Linux OS through arduino connected via USB

## Requirements:
1. gphoto2 must be compiled with supported camera connected via USB
2. Adafruit motor sheild for Arduino v2 drivers must be installed in order to alter C script controlling motor
