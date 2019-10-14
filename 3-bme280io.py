
#Author(s): Brent Rubell for Adafruit Industries
#Copyright (c) 2018 Adafruit Industries
#Licensed under the MIT license.
#All text above must be included in any redistribution.

#Re edited by KFLMIAMI420

# BME280 on rasperry pi zero w running debian buster October, 2019
# Take readings from a BME280 Sensor attached to a Raspberry Pi Zero W 
# Print readings to Terminal Window 
# Upload readings to Adafruit IO IOT Portal
# Convert Raw readings from C to F
# Add Decimal to Altitude upload to IO Portal
# Add Humidity correction for Sensor Error



import time
import board
import busio
import adafruit_bme280

from Adafruit_IO import Client, Feed, RequestError
LOOP_DELAY = 35
ADAFRUIT_IO_KEY = 'launch codes'
ADAFRUIT_IO_USERNAME = 'wopr'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we already have the feeds, assign them.
    temperature_feed = aio.feeds('temperature2')
    humidity_feed = aio.feeds('humidity2')
    pressure_feed = aio.feeds('pressure2')
    altitude_feed = aio.feeds('altitude2')
except RequestError: # if we don't, create and assign them.
    temperature_feed = aio.create_feed(Feed(name='temperature2'))
    humidity_feed = aio.create_feed(Feed(name='humidity2'))
    pressure_feed = aio.create_feed(Feed(name='pressure2'))
    altitude_feed = aio.create_feed(Feed(name='altitude2'))

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure = 1017.21
while True:
    print('Reading sensors...')
    temperature_data = bme280.temperature
    # convert temperature (C->F)
    temperature_data = int(temperature_data) * 1.8 + 32
    humid_data = bme280.humidity
    # humidity correction for sensor error. for better  readings get readings from DHT22 humidity on this hat
    humid_data = int(humid_data) + 6  
    pressure_data = bme280.pressure
    alt_data = bme280.altitude

    print('sending BME280 data to adafruit io...')
    print('Temperature: %0.1f F' % temperature_data)
    aio.send(temperature_feed.key, '{0:.2f} F'.format(temperature_data))
    print("Humidity: %0.1f %%" % humid_data)
    aio.send(humidity_feed.key, '{0:.2f} Percent '.format(humid_data))
   #time.sleep(2)
    print("Pressure: %0.1f hPa" % pressure_data)
    aio.send(pressure_feed.key, '{0:.2f} Mbar'.format(pressure_data))
    print("Altitude = %0.2f meters" % alt_data)
    aio.send(altitude_feed.key, '{0:.2f} meters'.format(alt_data))


    time.sleep(LOOP_DELAY * 1.2)
