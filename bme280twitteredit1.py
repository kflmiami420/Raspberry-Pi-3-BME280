# palmPi code written by Michael Horne
# @recantha
# www.recantha.co.uk/blog
# March 2018

# import libraries

import ifaddr
from time import sleep, strftime
import math
import bme280
from subprocess import call
import threading
#from twython import Twython
#from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

def read_temperature():
    temperature,pressure,humidity = bme280.readBME280All()
    temperature = (temperature * 1.8) + 32

    return "{:+.2f}".format(temperature)

# Function to read pressure from BMP280
def read_external_pressure():
    temperature,pressure,humidity = bme280.readBME280All()
    pressure = "{:.2f}".format(pressure)
    return pressure

#    Update = True

    try:
        twitter_status = get_timestamp() + " - Update - " + reasonf
        twitter.update_status(status=twitter_status)

    except:
        print("Failed to send tweet")

exit(1)

# Get sensor readings and send to the streamer
def stream_readings():
    while True:
        temperature_f, = read_temperature()
        pressure = read_pressure()
        print("Temp")
        streamer_log("Temp F", temerature)
        print("Pressure")
        streamer_log("Pressure", pressure)
        streamer.flush()

        try:
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

# Start Twitter client
#try:
#    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
#    twitter_status = "palmPi started up at " + get_timestamp()
#    twitter.update_status(status=twitter_status)
#    log("Twitter client started")

#except:
#    print("Twython did not tweet")
#    log("Twitter client did not start"
