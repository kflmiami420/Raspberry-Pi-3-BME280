# Raspberry-Pi-3-BME280

# please use freely on your project and share your code to help others 

# this will print a box with temperature in F
# this will print a box with temperature in C
# this will print a box with pressure in inHG 
# this will print a box with pressure in Mbar
# this will print a box with pressure in hpa
# this will print a box with humidity in % number 
# formulas to convert temps are below 
# formulas to convert temps are below


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
