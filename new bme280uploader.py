#https://www.instructables.com/id/Weather-Station-Using-Raspberry-Pi-With-BME280-in-/
#https://github.com/ControlEverythingCommunity/BME280/blob/master/Python/BME280.py

# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# BME280

# This code is designed to work with the BME280_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Humidity?sku=BME280_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# BME280 address, 0x76(118)
# Read data back from 0x88(136), 24 bytes
b1 = bus.read_i2c_block_data(0x76, 0x88, 24)

# Convert the data
# Temp coefficients
dig_T1 = b1[1] * 256 + b1[0]
dig_T2 = b1[3] * 256 + b1[2]
if dig_T2 > 32767 :
    dig_T2 -= 65536
dig_T3 = b1[5] * 256 + b1[4]
if dig_T3 > 32767 :
    dig_T3 -= 65536

# Pressure coefficients
dig_P1 = b1[7] * 256 + b1[6]
dig_P2 = b1[9] * 256 + b1[8]
if dig_P2 > 32767 :
    dig_P2 -= 65536
dig_P3 = b1[11] * 256 + b1[10]
if dig_P3 > 32767 :
    dig_P3 -= 65536
dig_P4 = b1[13] * 256 + b1[12]
if dig_P4 > 32767 :
    dig_P4 -= 65536
dig_P5 = b1[15] * 256 + b1[14]
if dig_P5 > 32767 :
    dig_P5 -= 65536
dig_P6 = b1[17] * 256 + b1[16]
if dig_P6 > 32767 :
    dig_P6 -= 65536
dig_P7 = b1[19] * 256 + b1[18]
if dig_P7 > 32767 :
    dig_P7 -= 65536
dig_P8 = b1[21] * 256 + b1[20]
if dig_P8 > 32767 :
    dig_P8 -= 65536
dig_P9 = b1[23] * 256 + b1[22]
if dig_P9 > 32767 :
    dig_P9 -= 65536

# BME280 address, 0x76(118)
# Read data back from 0xA1(161), 1 byte
dig_H1 = bus.read_byte_data(0x76, 0xA1)

# BME280 address, 0x76(118)
# Read data back from 0xE1(225), 7 bytes
b1 = bus.read_i2c_block_data(0x76, 0xE1, 7)

# Convert the data
# Humidity coefficients
dig_H2 = b1[1] * 256 + b1[0]
if dig_H2 > 32767 :
    dig_H2 -= 65536
dig_H3 = (b1[2] &  0xFF)
dig_H4 = (b1[3] * 16) + (b1[4] & 0xF)
if dig_H4 > 32767 :
    dig_H4 -= 65536
dig_H5 = (b1[4] / 16) + (b1[5] * 16)
if dig_H5 > 32767 :
    dig_H5 -= 65536
dig_H6 = b1[6]
if dig_H6 > 127 :
    dig_H6 -= 256

# BME280 address, 0x76(118)
# Select control humidity register, 0xF2(242)
#		0x01(01)	Humidity Oversampling = 1
bus.write_byte_data(0x76, 0xF2, 0x01)
# BME280 address, 0x76(118)
# Select Control measurement register, 0xF4(244)
#		0x27(39)	Pressure and Temperature Oversampling rate = 1
#					Normal mode
bus.write_byte_data(0x76, 0xF4, 0x27)
# BME280 address, 0x76(118)
# Select Configuration register, 0xF5(245)
#		0xA0(00)	Stand_by time = 1000 ms
bus.write_byte_data(0x76, 0xF5, 0xA0)

time.sleep(0.5)

# BME280 address, 0x76(118)
# Read data back from 0xF7(247), 8 bytes
# Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
# Temperature xLSB, Humidity MSB, Humidity LSB
data = bus.read_i2c_block_data(0x76, 0xF7, 8)

# Convert pressure and temperature data to 19-bits
adc_p = ((data[0] * 65536) + (data[1] * 256) + (data[2] & 0xF0)) / 16
adc_t = ((data[3] * 65536) + (data[4] * 256) + (data[5] & 0xF0)) / 16

# Convert the humidity data
adc_h = data[6] * 256 + data[7]

# Temperature offset calculations
var1 = ((adc_t) / 16384.0 - (dig_T1) / 1024.0) * (dig_T2)
var2 = (((adc_t) / 131072.0 - (dig_T1) / 8192.0) * ((adc_t)/131072.0 - (dig_T1)/8192.0)) * (dig_T3)
t_fine = (var1 + var2)
cTemp = (var1 + var2) / 5120.0
fTemp = cTemp * 1.8 + 32

# Pressure offset calculations
var1 = (t_fine / 2.0) - 64000.0
var2 = var1 * var1 * (dig_P6) / 32768.0
var2 = var2 + var1 * (dig_P5) * 2.0
var2 = (var2 / 4.0) + ((dig_P4) * 65536.0)
var1 = ((dig_P3) * var1 * var1 / 524288.0 + ( dig_P2) * var1) / 524288.0
var1 = (1.0 + var1 / 32768.0) * (dig_P1)
p = 1048576.0 - adc_p
p = (p - (var2 / 4096.0)) * 6250.0 / var1
var1 = (dig_P9) * p * p / 2147483648.0
var2 = p * (dig_P8) / 32768.0
pressure = (p + (var1 + var2 + (dig_P7)) / 16.0) / 100

# Humidity offset calculations
var_H = ((t_fine) - 76800.0)
var_H = (adc_h - (dig_H4 * 64.0 + dig_H5 / 16384.0 * var_H)) * (dig_H2 / 65536.0 * (1.0 + dig_H6 / 67108864.0 * var_H * (1.0 + dig_H3 / 67108864.0 * var_H)))
humidity = var_H * (1.0 -  dig_H1 * var_H / 524288.0)
if humidity > 100.0 :
    humidity = 100.0
elif humidity < 0.0 :
    humidity = 0.0

# Output data to screen
print "Temperature in Celsius : %.2f C" %cTemp
print "Temperature in Fahrenheit : %.2f F" %fTemp
print "Pressure : %.2f hPa " %pressure
print "Relative Humidity : %.2f %%" %humidity

import requests
from Adafruit_BME280 import *
from datetime import datetime

station_ID = "kflmiami444"
station_KEY = "7xpgwxm2"
log_file = "/tmp/wxlog.txt"
base_URL = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php"
software_type = "WU_Upload-v" + version
print("Reading sensor...")
# Init sensor
b1 = BME280(mode=BME280_OSAMPLE_8)
# Read data from sensor
b1_temp = sensor.read_temperature_f()
b1_humd = sensor.read_humidity()
b1_baro = sensor.read_pressure_inches()
b1_dewp = sensor.read_dewpoint_f()

# Build first half of POST
post_URL = base_URL+"?ID="+station_ID+"&PASSWORD="+station_KEY+"&dateutc=now"
# Fill dictionary with variables
payload = {"tempf": sensor_temp, "humidity": sensor_humd, "baromin": sensor_baro,\
    "dewptf": sensor_dewp, "softwaretype": software_type, "version": version,\
    "action": "updateraw"}
# Open log file for writing
print("Writing to log file...")
logfile = open(log_file, 'a')

# Write current time to log
logfile.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": ")

# Push data, exit on error
print("Connecting to Weather Underground...")
try:
    wu_push = requests.get(post_URL, params=payload, timeout=15)
except requests.exceptions.Timeout:
    print("Timeout!")
    logfile.write("Timeout!\n")
    logfile.close()
    exit()
except requests.exceptions.ConnectionError:
    print("Network Error!")
    logfile.write("Network Error!\n")
    logfile.close()
    exit()
except requests.exceptions.RequestException as e:
    print("Unknown Error!")
    logfile.write("Unknown Error!\n")
    logfile.close()
    exit()

# See if there was a good connection
if wu_push.status_code != 200:
    print("Error communicating with server!")
    logfile.write("Server Error!")
    logfile.write("\n")
    logfile.close()
    exit()

# Check response
if "success" in wu_push.text:
    # Print status message and write conditions to log
    print("Upload OK!")
    condition_string = str("{:.2f} F".format(sensor_temp))+", "+str("{:.2f}%".format(sensor_humd))+", "+\
        str("{:.2f} in".format(sensor_baro))
    logfile.write(condition_string)
elif "Password" in wu_push.text:
    print("Station ID or password error!")
    logfile.write("Authentication Error!")
else:
    print("Invalid response!")
    logfile.write("Unknown Error!")

# Close file and print message
logfile.write("\n")
logfile.close()
print("Done")

# EOF


