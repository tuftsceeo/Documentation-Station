# Documentation-Station
Most recent version updated by 2017 CEEO Winterns (Fiona, Ashwin, and Ryan) is "docstation_2.0.py". Ensure all the directories you are saving photos to match the filepaths in this file.

Any python script name including dropbox or USB was developed by summer intern Michael Pine so that the user had options of where to save the photos (locally or to the cloud) based on preference and/or internet accessibility. Unfortunately, the Dropbox API is difficult to customize on the Pi with a different user account other than the developer (in this case, being Michael). Ideally would want to customize it to be more "plug and play" in the future for any teachers hoping to leverage this capability.

The program "master.py" should be used in juncture with the USB vs dropbox py scripts since it determines the internet status of the pi upon start-up and which programs to run.

The following includes sytem requirements/necassary installations:

  First, enter: sudo apt-get install motion . 
  Then we will edit the motion.conf file by typing: sudo nano /etc/motion/motion.conf
  This is quite a large conf file but the point you need to edit is:
  DAEMON = OFF (change to ON)
  Next, open the /motion file by typing: sudo nano /etc/default/motion
  And edit the following:
  start_motion_daemon = no (change to yes)
  Now, download the file “docstation_aug.py” from github: sudo git clone
  https://github.com/smbitetti/Documentation-Station/blob/master/docstation_aug.py
  Move this file from your downloads folder to /home/pi: sudo mv /home/pi/downloads/docstation_aug.py /home/pi/docstation_aug.py Make sure there are no permission restrictions on this file by lastly typing sudo chmod 755 /home/pi/docstation_aug.py.

  If you are using the LCD 7inch touchscreen instead of a desktop monitor, you will need to reconfigure one file in addition to having a USB power hub, as the raspberry pi does not provide enough power to the touchscreen on it’s own. 
  sudo nano /boot/config.txt
  Edit this configuration file to match the code below:

  # uncomment if hdmi display is not detected and composite is being output
  hdmi_force_hotplug=1

  # uncomment to force a specific HDMI mode (here we are forcing 800x480!)
  hdmi_group=2
  hdmi_mode=1
  hdmi_mode=87
  hdmi_cvt=800 480 60 6 0 0 0

  max_usb_current=1
  
  For ability to access the photos over local webserver, visit instructions under start-up guide (will need to install apache and php packages)
