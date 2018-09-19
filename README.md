# Raspberry-Pi-3-BME280

This are sample simple programs that help you test your bme280 sensor   Temp / Press / Humi  (very similar to BMP280)

These examples are for I2C type conncetions   

Pi 3V3 to sensor VIN
Pi GND to sensor GND
Pi SCL to sensor SCK
Pi SDA to sensor SDI


#temperature formulas 
degrees        =   sensor.read_temperature()
degrees        =   (degrees * 1.8) + 32
degrees2       =   sensor.read_temperature()
degrees2       =   degrees2
#pressure formulas
pascal         =   sensor.read_pressure()
inchesHG       =   (pascal /3386.39)
mbar           =   (inchesHG * 33.8639)
humidity       =   sensor.read_humidity()
