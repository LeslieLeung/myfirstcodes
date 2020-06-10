# -*- coding:utf-8 -*-
import time as fk
import subprocess
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
from datetime import *
import Adafruit_DHT

serial = spi(device=0, port=0)
device = ssd1306(serial)
sensor = Adafruit_DHT.DHT11
gpio = 4

while True:
    #get systeminfo
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    date = datetime.now()
    date_f = date.strftime('%Y-%m-%d')
    time_f = date.strftime('%x %H:%M:%S %p')
    # get tempreture and humidity
    humidity, temp = Adafruit_DHT.read_retry(sensor, gpio)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((2, 2) , "IP: "+str(IP), fill="white")
        draw.text((2, 13),  str(CPU), fill="white")
        draw.text((2, 24), str(MemUsage), fill="white")
        #draw.text((1, 30), str(Disk), fill="white")
        #draw.text((0, 33), str(date_f), fill="white")
        #draw.text((0, 35), str(time_f), fill="white")
        draw.text((0, 35), "------------------------------", fill="white")
        draw.text((2, 43), "Tempreture: "+str(temp), fill="white")
        draw.text((2, 51), "Humidity: "+str(humidity), fill="white")
    
    fk.sleep(3)
    #pass

