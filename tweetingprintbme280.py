# Sept 2018

# import libraries
import time
import os
import ifaddr
from time import sleep, strftime
import math
import bme280
from gpiozero import LED, Button
from subprocess import call
from ISStreamer.Streamer import Streamer
import threading
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

# Function to read temperature from BMP280 and convert it to F
def read_external_temperature():
    temp_c,pressure,humidity = bme280.readBME280All()
    temp_f = (temp_c * 1.8) + 32

    return "{:+.2f}".format(temp_c), "{:+.2f}".format(temp_f)

Shutting_down = True

    try:
        twitter_status = get_timestamp() + " - Shutting down - " + reason
        twitter.update_status(status=twitter_status)

    except:
        print("Failed to send tweet")

            twitter_status = get_timestamp() + " - Int temp: " + str(i_temp_c) + "C / Ext temp:" + str(e_temp_c) + "C / Pressure: " + str(e_pressure) + "hPa"
            log("Attempting to tweet - " + twitter_status)
            twitter.update_status(status=twitter_status)

        except:
            print("Twython did not tweet")
            log("Twython did not tweet")

        print("Sleeping for 15 minutes")
        sleep(900)

# Twitter detects repetition, so timestamp the tweets to prevent them reading as duplicates
def get_timestamp():
    timestamp = strftime("%Y%m%d-%H:%M:%S")

    return timestamp

def log(msg):
    path = '/home/pi/palmPi/palmPi.log'
    log_file = open(path, 'a')
    log_file.write(get_timestamp() + ":" + msg + "\n")
    log_file.close()

# Start up logging
log("Started up palmPi")

# Start Twitter client
try:
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    twitter_status = "palmPi started up at " + get_timestamp()
    twitter.update_status(status=twitter_status)
    log("Twitter client started")

except:
    print("Twython did not tweet")
    log("Twitter client did not start")

# Start up the 15-minute looping thread for streaming and tweeting readings
thread_readings = readingThread(1, "Reading-Thread", 1)
thread_readings.start()
log("Started readings thread")
log("Going into main loop")

flag is not set, get readings and spit them out onto LCD
    if not shutting_down:
        # Show the IP addresses of palmPi
        addrs = read_ip_addresses()
        for addr in addrs:
            lcd.write_string(addr)
            print(addr)
            sleep(1)
            lcd.clear()

        # Read and display internal temperature
        for i in range(0,10):
            temp_c, temp_f = read_internal_temperature()

            lcd.write_string("Int: ")
            lcd.write_string(str(temp_c))
            lcd.write_string("C")
            lcd.cursor_pos = (1,0)
            lcd.write_string("Int: ")
            lcd.write_string(str(temp_f))
            lcd.write_string("F")
            print("Int temp: ", temp_c, " C")
            print("Int temp: ", temp_f, " F")

            sleep(0.5)
            lcd.clear()
 
        # Read and display external temperature
        for i in range(0,10):
            temp_c, temp_f = read_external_temperature()
            lcd.write_string("Ext: ")
            lcd.write_string(str(temp_c))
            lcd.write_string("C")
            lcd.cursor_pos = (1,0)
            lcd.write_string("Ext: ")
            lcd.write_string(str(temp_f))
            lcd.write_string("F")

            print("Ext temp: ", temp_c, " C")
            print("Ext temp: ", temp_f, " F")

            sleep(0.5)
            lcd.clear()

        # Read and display external pressure reading
        for i in range(0,10):
            pressure = read_external_pressure()
            lcd.write_string("Pres: ")
            lcd.write_string(str(pressure))
            lcd.write_string("hPa")
            print("Pressure: ", pressure, " hPa")

            sleep(0.5)
            lcd.clear()
            
            import bme280
 
(chip_id, chip_version) = bme280.readBME280ID()
print "Chip ID :", chip_id
print "Version :", chip_version
 
temperature,pressure,humidity = bme280.readBME280All()
 
print "Temperature : ", temperature, "C"
print "Pressure : ", pressure, "hPa"
print "Humidity : ", humidity, "%"
