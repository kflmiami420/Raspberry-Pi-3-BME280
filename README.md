BME280 Sensor Driver
====================
.. image:: https://travis-ci.org/rm-hull/bme280.svg?branch=master
   :target: https://travis-ci.org/rm-hull/bme280

.. image:: https://coveralls.io/repos/github/rm-hull/bme280/badge.svg?branch=master
   :target: https://coveralls.io/github/rm-hull/bme280?branch=master

.. image:: https://img.shields.io/pypi/pyversions/rpi-bme280.svg
   :target: https://pypi.python.org/pypi/rpi-bme280

.. image:: https://img.shields.io/pypi/v/rpi-bme280.svg
   :target: https://pypi.python.org/pypi/rpi-bme280

.. image:: https://img.shields.io/maintenance/yes/2018.svg?maxAge=2592000


Interfacing a Bosch BME280 digital sensor module (capable of sensing
temperature, humidity and pressure) in Python 2 or 3 using I2C on the Raspberry
Pi. The particular kit I bought can be acquired for a few pounds from `eBay
<http://www.ebay.co.uk/itm/311728184519>`_. Further technical details for the
BME280 sensor can be found in the `datasheet
<https://raw.githubusercontent.com/rm-hull/bme280/master/doc/tech-spec/BME280.pdf>`_
[PDF].

.. image:: https://raw.githubusercontent.com/rm-hull/bme280/master/doc/bme280-sensor.jpg
   :alt: mounted

GPIO pin-outs
-------------
The BME280 is an I2C device, so connecting to the RPi is very straightforward:

P1 Header
^^^^^^^^^
For prototyping, the P1 header pins should be connected as follows:

========== ====== ============ ======== ==============
Board Pin  Name   Remarks      RPi Pin  RPi Function  
========== ====== ============ ======== ==============
1          VIN    +3.3V Power  P01-1    3V3           
2          GND    Ground       P01-6    GND           
3          SCL    Clock        P01-5    GPIO 3 (SCL)  
4          SDA    Data         P01-3    GPIO 2 (SDA)  
========== ====== ============ ======== ==============

Pre-requisites
--------------
Ensure that the I2C kernel driver is enabled::

  $ dmesg | grep i2c
  [    4.925554] bcm2708_i2c 20804000.i2c: BSC1 Controller at 0x20804000 (irq 79) (baudrate 100000)
  [    4.929325] i2c /dev entries driver

or::

  $ lsmod | grep i2c
  i2c_dev                 5769  0
  i2c_bcm2708             4943  0
  regmap_i2c              1661  3 snd_soc_pcm512x,snd_soc_wm8804,snd_soc_core

If you have no kernel modules listed and nothing is showing using ``dmesg`` then this implies
the kernel I2C driver is not loaded. Enable the I2C as follows:

#. Run ``sudo raspi-config``
#. Use the down arrow to select ``9 Advanced Options``
#. Arrow down to ``A7 I2C``
#. Select **yes** when it asks you to enable I2C
#. Also select **yes** when it asks about automatically loading the kernel module
#. Use the right arrow to select the **<Finish>** button
#. Select **yes** when it asks to reboot

After rebooting re-check that the ``dmesg | grep i2c`` command shows whether
I2C driver is loaded before proceeding.

Optionally, to improve permformance, increase the I2C baudrate from the default
of 100KHz to 400KHz by altering ``/boot/config.txt`` to include::

  dtparam=i2c_arm=on,i2c_baudrate=400000

Then reboot.

Then add your user to the i2c group::

  $ sudo adduser pi i2c

Install some packages::

  $ sudo apt-get install i2c-tools python-pip

Next check that the device is communicating properly (if using a rev.1 board,
use 0 for the bus not 1)::

  $ i2cdetect -y 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- 76 --

Installing the Python Package
-----------------------------
For python2, from the bash prompt, enter::

  $ sudo python setup.py install

This will install the Python files in ``/usr/local/lib/python2.7``
making them ready for use in other programs.

Alternatively for python3, type::

 $ sudo python3 setup.py install

Cheeseshop install
^^^^^^^^^^^^^^^^^^
Alternatively, a version on PyPi is available, just do::

  $ sudo pip install RPi.bme280

Software Driver - Example Usage
-------------------------------
Once installed, confirm the I2C address (see prerequisites, it will most 
likely be 0x76 or 0x77) and port.

Then in a python script or REPL:

.. code:: python

  import smbus2
  import bme280

  port = 1
  address = 0x76
  bus = smbus2.SMBus(port)

  calibration_params = bme280.load_calibration_params(bus, address)

  # the sample method will take a single reading and return a
  # compensated_reading object
  data = bme280.sample(bus, address, calibration_params)

  # the compensated_reading class has the following attributes
  print(data.id)
  print(data.timestamp)
  print(data.temperature)
  print(data.pressure)
  print(data.humidity)

  # there is a handy string representation too
  print(data)

This then should print something like::

  ee50df9c-3aa3-4772-8767-73b6bb74f30f
  2016-11-18 17:33:28.937863
  20.563
  980.91
  48.41
  compensated_reading(id=ee50df9c-3aa3-4772-8767-73b6bb74f30f, 
      timestamp=2016-11-18 17:33:28.937863, temp=20.563 °C, 
      pressure=980.91 hPa, humidity=48.41 % rH)

For a data-logger like application, periodically call ``bme2.sample(bus, address, calibration_params)`` to
get time-based readings.

See the `weatherstation project <https://github.com/rm-hull/weatherstation>`_ for
a more complete example usage.

References
----------
> TODO

------------------------------------------------------------------------------------------------------------------------









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



Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-bme280/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/bme280/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.org/adafruit/Adafruit_CircuitPython_BME280.svg?branch=master
    :target: https://travis-ci.org/adafruit/Adafruit_CircuitPython_BME280
    :alt: Build Status

I2C and SPI driver for the Bosch BME280 Temperature, Humidity, and Barometric Pressure sensor

Installation and Dependencies
=============================

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure that the driver and all dependencies are available on the
CircuitPython filesystem.  This can be most easily achieved by downloading and
installing the latest
`Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_
on your device.

Installing from PyPI
--------------------

On the Raspberry Pi, you can install the driver locally
`from PyPI <https://pypi.org/project/adafruit-circuitpython-bme280/>`_.  To
install system-wide, use:

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-bme280

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-bme280

Usage Example
=============

.. code-block:: python

    import board
    import digitalio
    import busio
    import time
    import adafruit_bme280

    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    # OR create library object using our Bus SPI port
    #spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    #bme_cs = digitalio.DigitalInOut(board.D10)
    #bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1013.25

    while True:
        print("\nTemperature: %0.1f C" % bme280.temperature)
        print("Humidity: %0.1f %%" % bme280.humidity)
        print("Pressure: %0.1f hPa" % bme280.pressure)
        print("Altitude = %0.2f meters" % bme280.altitude)
        time.sleep(2)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BME280/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building Locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip3 install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-veml6070 --library_location .

Sphinx Documentation
--------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip3 install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
