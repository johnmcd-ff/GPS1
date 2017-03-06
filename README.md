John McDermott


This LoPy project uses a GPS receiver and sends the location data from LoPy device #1 to LoPy device#2, then posts to the internet using MQTT protocol.  Owntracks is used as a mqtt client to map the GPS points.


GPS RX --> LoPy1 > - - - >  LoPy2 (mqtt-wifi) > - - > R Pi (mqtt broker) > - - > Owntracks Android mqtt map


Files in project:

boot.py   # unmodified pycom boot file

main.py   # set's up wifi and connects to local network if available
          # updates real time clock from ntp.  Not strictly necessary and may be omitted
          # calls the module to handle GPS and Lora.
          # use one of the following lines, leave the other as comment, flash one version of each main.py into each LoPy device.
          # either:
          # execfile('/flash/LoRaGPS.py')      			# run GPS and Lora loop to transmit, use this command for sending GPS unit
          # execfile('/flash/LoRaGPSpost.py')			# run Lora loop to receive and post to mqtt

homewifi/homewifi.py  # connect to local wifi if available.
homewifi/ntp_time.py  # update real time clock using ntp.  Not strictly necessary and may be left out if desired.
homewifi/wifi_name.txt  # file containing SSID and password for connecting to wifi.  This file must be created and saved to flash.  This method done to avoid putting SSID/password in source code files.

gps.py    # module to convert data from GPS receiver into object containing required data.  Thanks to Peter Affolter for this code.

LoRaGPS.py  # module used by LoPy that has GPS receiver and will transmit data to home base LoPy
LoRaGPSpost.py  # module used by home base LoPy to receive LoRa data containing GPS information, then post using mqtt to broker server.


This example assumes a mqtt server hosted locally, (for example Raspberry Pi with mosquitto installed - there are plenty of tutorials for installing and testing, note if you have wheezy or jessie verions of Raspian)

I have also used the Owntracks app for mapping the data, and connected using the private mqtt setting.
refer to:
http://owntracks.org/
http://owntracks.org/booklet/
http://owntracks.org/booklet/guide/mqtt/

When testing the setup it is useful to compare the console output from each LoPy, and also on the Raspberry Pi to view using the command:  mosquitto_sub -v -t '#'
This checks that GPS data is being generated, the second LoPy is receiving, and that the mqtt broker is getting messages.
