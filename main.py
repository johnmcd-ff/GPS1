# main.py -- put your code here!
import time
#from LoRaGPS import GPS_run

print('main')
time.sleep(5)
print('start wifi')
execfile('/flash/homewifi/homewifi.py')		# connect to wifi
time.sleep(2)
execfile('/flash/homewifi/ntp_time.py')		# update RTC
execfile('/flash/LoRaGPS.py')      			# run GPS and Lora loop to transmit, use this command for sending GPS unit
#execfile('/flash/LoRaGPSpost.py')			# run Lora loop to receive and post to mqtt

