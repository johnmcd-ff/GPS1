from network import LoRa
import socket
import machine
import time
import pycom
import struct
import json
from network import WLAN
from simple import  MQTTClient

#from umqtt.simple import 
def mqttopen():
    print("mqtt Started")
    client = MQTTClient("j2", "192.168.1.129", port=1883)	# pulish to mosquitto running on Raspberry Pi
        client.connect()
    print("mqtt connected")
    return(client)
	
	
def LoraDemoRun():
    
    #set to have no heart beat
    pycom.heartbeat(False)

    # initialize LoRa in LORA mode
    lora = LoRa(mode=LoRa.LORA, frequency=925000000)

    # create a raw LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setblocking(False)
    
    client = mqttopen()
        
    json_msg = {}
    json_msg['_type'] = 'location'
    json_msg['tid'] = 'J2'
    json_msg['lat'] = 0.0
    json_msg['lon'] = 0.0
    json_msg['tst'] = 0
    
    
    print("Started")
    while True:
        # wait to receive data
        time.sleep(1)
        data = s.recv(64)
        
        #if Data has been received
        if data != b'':
            print(data)
            uDataGps = struct.unpack("ii",  data)
            print(uDataGps[0]/100000,  uDataGps[1]/100000)
            pycom.rgbled(0x007f00) # green
            time.sleep(1)
            json_msg['lon'] = uDataGps[0]/100000
            json_msg['lat'] = uDataGps[1]/100000
            json_msg['tst'] = time.time()
            json_str = json.dumps(json_msg)
            print (json_str)
            client.publish('owntracks/john/j2',  json_str)    # disable mqtt on the sending unit
            pycom.rgbled(0x7f0000) # red
            

LoraDemoRun()   
        
