
import tweepy, time, sys
from Adafruit_BME280 import *#https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/wiring-and-test
from datetime import datetime

#--------------------------------------------------------------------
CONSUMER_KEY = 'H2OaDt1 SECRET CODE GOES HERE smFrlPOzr6EbA'
CONSUMER_SECRET = 'F7slLnT5 SECRET CODE GOES HERE owFLhSsrhhTM8kErWpLDrGngwahizaDRtNXrgR'
ACCESS_KEY = '10171991 SECRET CODE GOES HERE 36121217026-fX37Uf2m7hXcuLnD9ekdFCrL1znxdz'
ACCESS_SECRET = 'Op1lMH6sS6GSECRET CODE GOES HERE RYMaRmeyGlCvKmc0sXKCWDz9ezNS4NySwe'
#--------------------------------------------------------------------

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

TweetsThisRun = 1;
try:
  while True:
    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    degrees        =    sensor.read_temperature()
    degrees        =   (degrees * 1.8) + 32
    pascals        =    sensor.read_pressure()
    inchesHG       =   (pascals /3386.39)
    mbar           =   (inchesHG * 33.8639)
    hectopascals   =    pascals / 100
    humidity       =    sensor.read_humidity()


    DateTweeted = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    TweetTemperatureString = 'Temperature {1:0.2f}F                             Pressure {2:0.2f} inHg                              Pressure {3:0.0f} Mbar             $

    print "Writing Tweet {} @ {} \n\tTweet: {}".format(TweetsThisRun, DateTweeted, TweetTemperatureString)
    api.update_status(TweetTemperatureString)
    TweetsThisRun += 1
    time.sleep(900)
except KeyboardInterrupt:
  print "Exiting."
