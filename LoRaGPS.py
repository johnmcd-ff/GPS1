import machine
import time
import pycom
import socket
import struct
import json
from network import LoRa
from gps import GPS_UART_start
from gps import NmeaParser
from simple import MQTTClient

rtc = machine.RTC()


def sendtoLoRa(s,  dev_ID,  place):
    # send some data

    dev_time = rtc.now()

    datatosend = struct.pack('ii', int(place.longitude*100000),  int(place.latitude*100000))
    print('LoRa send: {}\n'.format(datatosend))
    s.setblocking(True)
    s.send(datatosend)
    s.setblocking(False)

    pycom.rgbled(0x001f00)  # LoRa heartbeat LED on

    time.sleep(2)			# pause 2s for next read
    pycom.rgbled(0x00001f)  # LoRa heartbeat LED off


def GPS_run():
    print ('GPS_run')
    pycom.heartbeat(False)      # turn off the heartbeat LED so that it can be reused
    pycom.rgbled(0x000000)    # turn LED off
    print('GPS start')

    f=open('device_name')   #get device name from file
    dev_ID = f.read()
    print(dev_ID)

    # connect to GPS device
    com = GPS_UART_start()

    # initialize LoRa in LORA mode
    # more params can also be given, like frequency, tx power and spreading factor
    print ("LoRa start")
    lora = LoRa(mode=LoRa.LORA,  frequency=925000000,  tx_power=20)

    # create a raw LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    while True:
        if (com.any()):
            data =com.readline()
            #print (data)

            if (data[0:6] == b'$GPGGA'):
                place = NmeaParser()
                place.update(data)
                print ("place", place.longitude,  ":",  place.latitude,  ":", place.fix_time)
                sendtoLoRa(s,  dev_ID,  place)
   
                # f_log = open('Lora_log','a')  # careful that log file fills up the memory
                # f_log.write(data + ' ' + str(lora.rssi()) + '\n\n')
                # f_log.close()
                # wait a random amount of time
                time.sleep(10 + (machine.rng() & 0x3f)/10)
    

print('Lora Run')
GPS_run()
