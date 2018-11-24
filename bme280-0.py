#
#bme280final.py
#xbme280final.py
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280$

degrees        =   sensor.read_temperature()
degrees        =   (degrees * 1.8) + 32
pascal         =   sensor.read_pressure()
inchesHG       =   (pascal /3386.39)
mbar           =   (inchesHG * 33.8639) 
humidity       =   sensor.read_humidity()
print '-----------------------------'
print 'Temperature    = {0:0.2f} deg F'.format(degrees)
print 'Pressure       = {0:0.2f} inHg'.format(inchesHG)
print 'Pressure       = {0:0.2f} Mbar' .format(mbar)
print 'Pressure       = {0:0.2f} hPa  '.format(pascal)
print 'Humidity       = {0:0.2f} %'    .format(humidity)
print '-----------------------------'

