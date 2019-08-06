# bme280 simple script   to read sensor then convert C to F      and then print both readings  
# bme280 simple script   to read sensor then conver
# uses Adafruit_BME280 library
#
#
import bme280
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

degrees      =  sensor.read_temperature()
degrees2     =  sensor.read_temperature()
pascals      =  sensor.read_pressure()
hectopascals =  (pascals / 100) / 33.9

humidity     =   sensor.read_humidity()

degrees      =   (degrees * 1.8) + 32
degrees2     =   degrees2

print '-----------------------------'
print 'Temperature  = {0:0.2f} deg F'.format(degrees)
print 'Temperature  = {0:0.2f} deg C'.format(degrees2)
print 'Pressure     = {0:0.2f} inHg'.format(hectopascals)
print 'pressure     = {0:0.2f} hPa'.format(pascals)
print 'Humidity     = {0:0.2f} %'.format(humidity)
print '-----------------------------'


