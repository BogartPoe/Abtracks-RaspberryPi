# This File will upload the GPS cordinates (ie, Lat and Long) to the Thingspeak IoT Platform
# Provide your Thingspeak Write API key in the section provided below
# pynmea2 is Python library for parsing the NMEA 0183 protocol (GPS). To get that thing : pip install pynmea2
# Run this program on Raspberry Pi

import httplib, urllib
import time,random
import threading, os, time, pynmea2
from GPS_API import *
import serial, string
ser = serial.Serial("/dev/ttyAMA0")  # Select your Serial Port
ser.baudrate = 9600  # Baud rate
ser.timeout = 50
sleep = 60 # how many seconds to sleep between posts to the channel

key = '<Your Thinkspeak channel Key>'  # Thingspeak Write API Key
msgdata = Message() # Creates a Message Instance
 
# This Function will upload Latitude and Longitude values to the Thingspeak channel
def upload_cloud():
        temp = get_latitude(msgdata.msg)
        temp1 = get_longitude(msgdata.msg)
        params = urllib.urlencode({'field1': temp,'field2': temp1, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept" : "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print("Lat:",temp)
            print("Long:",temp1)
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"

if __name__ == "__main__":

        start_gps_receiver(ser, msgdata)
        print(msgdata.msg)
        time.sleep(2)
        ready_gps_receiver(msgdata)
        while True:
                upload_cloud()
                time.sleep(sleep)
