#get ntp time

# imports

from machine import RTC
import socket

print("ntp start")

def getNTPTime():
    host = "66.199.22.67" #"pool.ntp.org"
    rtc = RTC()
    
    # connect to server
    s=socket.socket()
    s.connect(socket.getaddrinfo(host,13)[0][-1])
    msgraw=s.recv(1024)
    msg = msgraw.decode()
    s.close()
    print(msg)
    year = 2000 + int(msg[6:9])
    month = int(msg[10:12])
    day = int(msg[13:15])
    hour = int(msg[16:18])
    min = int(msg[19:21])
    sec = int(msg[22:24])

    rtc = RTC()
    rtc.init((year, month, day, hour, min, sec, 0, 0))

    return(rtc)

now = RTC()
now = getNTPTime()
print(now.now())
print ("ntp end")

