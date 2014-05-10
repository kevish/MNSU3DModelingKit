import serial
import subprocess
import os

base_folder = "/artifacts"
catalog_number = str(raw_input('Please enter catalog number (e.g.2013.2.5):'))
number_of_photos = int(input('# of photos to take: '))
total_photos = number_of_photos

def trigger_capture(output_folder, filename, file_number, file_extension):
	output_filename = os.path.join(output_folder, filename + '_' + file_number + file_extension)
	trigger = 'gphoto2 --capture-image-and-download --filename %s' % output_filename
	os.system(trigger)
	print filename, 'captured!'

triggercapture = 'gphoto2 --capture-image-and-download --filename %s' % os.path.join(base_folder, catalog_number + ".jpg")
ser = serial.Serial('/dev/ttyACM0', 9600)
capture_number = 0
filename_number = 1
while number_of_photos > 0:
	print ser.read()
	print "waiting for serial input on port ACM0..."
        if ser.read() == "2":
                print "Serial input detected..."
		trigger_capture(base_folder, catalog_number,  str(filename_number), '.jpg')
		filename_number += 1

#                os.system(triggercapture)
#                print "Captured"
                number_of_photos = number_of_photos -1
                print "%s photos remaining of %s" % (number_of_photos, total_photos)
        elif number_of_photos == 0:
                ser.write("3")
                break
        else:
                print "unknown serial input"
