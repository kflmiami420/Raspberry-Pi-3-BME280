# THE SOFTWARE.
import logging
import time
import math
 # BME280 default address.
@@ -89,6 +90,7 @@
 class BME280(object):
    
    def __init__(self, t_mode=BME280_OSAMPLE_1, p_mode=BME280_OSAMPLE_1, h_mode=BME280_OSAMPLE_1,
                 standby=BME280_STANDBY_250, filter=BME280_FILTER_off, address=BME280_I2CADDR, i2c=None,
                 **kwargs):
@@ -264,16 +266,19 @@ def read_pressure_inches(self):
        pascals = self.read_pressure()
        inches = pascals * 0.0002953
        return inches
     
    def read_dewpoint(self):
        # Return calculated dewpoint in C, only accurate at > 50% RH
        # Return calculated dewpoint in C using the Magnus formula
        a = 17.271
        b = 237.7
        celsius = self.read_temperature()
        humidity = self.read_humidity()
        dewpoint = celsius - ((100 - humidity) / 5)
        gamma = (a * celsius /(b + celsius)) + math.log(humidity/100.0)
        dewpoint = (b * gamma) / (a - gamma)
        return dewpoint
         
    def read_dewpoint_f(self):
        # Return calculated dewpoint in F, only accurate at > 50% RH
        # Return calculated dewpoint in F using the Magnus formula
        dewpoint_c = self.read_dewpoint()
        dewpoint_f = dewpoint_c * 1.8 + 32
        return dewpoint_f
