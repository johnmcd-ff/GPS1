This LoPy project uses a GPS receiver and sends the location data from LoPy device #1 to LoPy device#2, then posts to the internet using MQTT protocol.  Owntracks is used as a mqtt client to map the GPS points.


GPS RX --> LoPy1 > - - - >  LoPy2 (mqtt-wifi) > - - > R Pi (mqtt broker) > - - > Owntracks Android mqtt map

