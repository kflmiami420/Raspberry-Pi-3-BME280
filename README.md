
      
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a id="user-content-bme280-sensor-driver" class="anchor" aria-hidden="true" href="#bme280-sensor-driver"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>BME280 Sensor Driver</h1>
<a href="https://travis-ci.org/rm-hull/bme280" rel="nofollow"><img alt="https://travis-ci.org/rm-hull/bme280.svg?branch=master" src="https://camo.githubusercontent.com/49993cd818e08d38f58dacd5457cca356d196cb2/68747470733a2f2f7472617669732d63692e6f72672f726d2d68756c6c2f626d653238302e7376673f6272616e63683d6d6173746572" data-canonical-src="https://travis-ci.org/rm-hull/bme280.svg?branch=master" style="max-width:100%;"></a>
<a href="https://coveralls.io/github/rm-hull/bme280?branch=master" rel="nofollow"><img alt="https://coveralls.io/repos/github/rm-hull/bme280/badge.svg?branch=master" src="https://camo.githubusercontent.com/1cfa792a2e5211362d15e4df11b8aaf8920ab66d/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f726d2d68756c6c2f626d653238302f62616467652e7376673f6272616e63683d6d6173746572" data-canonical-src="https://coveralls.io/repos/github/rm-hull/bme280/badge.svg?branch=master" style="max-width:100%;"></a>
<a href="https://pypi.python.org/pypi/rpi-bme280" rel="nofollow"><img src="https://camo.githubusercontent.com/ec7c78cae069a697093e74b65eec136e61417426/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f7270692d626d653238302e737667" data-canonical-src="https://img.shields.io/pypi/pyversions/rpi-bme280.svg" style="max-width:100%;">
</a>
<a href="https://pypi.python.org/pypi/rpi-bme280" rel="nofollow"><img src="https://camo.githubusercontent.com/1bb8445c122122fc8e03103de9371f2c7659f459/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7270692d626d653238302e737667" data-canonical-src="https://img.shields.io/pypi/v/rpi-bme280.svg" style="max-width:100%;">
</a>
<p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/dc889d2da526de91b68763154da8439e83368426/68747470733a2f2f696d672e736869656c64732e696f2f6d61696e74656e616e63652f7965732f323031382e7376673f6d61784167653d32353932303030"><img alt="https://img.shields.io/maintenance/yes/2018.svg?maxAge=2592000" src="https://camo.githubusercontent.com/dc889d2da526de91b68763154da8439e83368426/68747470733a2f2f696d672e736869656c64732e696f2f6d61696e74656e616e63652f7965732f323031382e7376673f6d61784167653d32353932303030" data-canonical-src="https://img.shields.io/maintenance/yes/2018.svg?maxAge=2592000" style="max-width:100%;"></a></p>
<p>Interfacing a Bosch BME280 digital sensor module (capable of sensing
temperature, humidity and pressure) in Python 2 or 3 using I2C on the Raspberry
Pi. The particular kit I bought can be acquired for a few pounds from <a href="http://www.ebay.co.uk/itm/311728184519" rel="nofollow">eBay</a>. Further technical details for the
BME280 sensor can be found in the <a href="https://raw.githubusercontent.com/rm-hull/bme280/master/doc/tech-spec/BME280.pdf" rel="nofollow">datasheet</a>
[PDF].</p>
<p><a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/rm-hull/bme280/master/doc/bme280-sensor.jpg"><img alt="mounted" src="https://raw.githubusercontent.com/rm-hull/bme280/master/doc/bme280-sensor.jpg" style="max-width:100%;"></a></p>
<a name="user-content-gpio-pin-outs"></a>
<h2><a id="user-content-gpio-pin-outs" class="anchor" aria-hidden="true" href="#gpio-pin-outs"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>GPIO pin-outs</h2>
<p>The BME280 is an I2C device, so connecting to the RPi is very straightforward:</p>
<a name="user-content-p1-header"></a>
<h3><a id="user-content-p1-header" class="anchor" aria-hidden="true" href="#p1-header"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>P1 Header</h3>
<p>For prototyping, the P1 header pins should be connected as follows:</p>
<table>







<thead valign="bottom">
<tr><th>Board Pin</th>
<th>Name</th>
<th>Remarks</th>
<th>RPi Pin</th>
<th>RPi Function</th>
</tr>
</thead>
<tbody valign="top">
<tr><td>1</td>
<td>VIN</td>
<td>+3.3V Power</td>
<td>P01-1</td>
<td>3V3</td>
</tr>
<tr><td>2</td>
<td>GND</td>
<td>Ground</td>
<td>P01-6</td>
<td>GND</td>
</tr>
<tr><td>3</td>
<td>SCL</td>
<td>Clock</td>
<td>P01-5</td>
<td>GPIO 3 (SCL)</td>
</tr>
<tr><td>4</td>
<td>SDA</td>
<td>Data</td>
<td>P01-3</td>
<td>GPIO 2 (SDA)</td>
</tr>
</tbody>
</table>
<a name="user-content-pre-requisites"></a>
<h2><a id="user-content-pre-requisites" class="anchor" aria-hidden="true" href="#pre-requisites"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Pre-requisites</h2>
<p>Ensure that the I2C kernel driver is enabled:</p>
<pre>$ dmesg | grep i2c
[    4.925554] bcm2708_i2c 20804000.i2c: BSC1 Controller at 0x20804000 (irq 79) (baudrate 100000)
[    4.929325] i2c /dev entries driver
</pre>
<p>or:</p>
<pre>$ lsmod | grep i2c
i2c_dev                 5769  0
i2c_bcm2708             4943  0
regmap_i2c              1661  3 snd_soc_pcm512x,snd_soc_wm8804,snd_soc_core
</pre>
<p>If you have no kernel modules listed and nothing is showing using <code>dmesg</code> then this implies
the kernel I2C driver is not loaded. Enable the I2C as follows:</p>
<ol>
<li>Run <code>sudo raspi-config</code></li>
<li>Use the down arrow to select <code>9 Advanced Options</code></li>
<li>Arrow down to <code>A7 I2C</code></li>
<li>Select <strong>yes</strong> when it asks you to enable I2C</li>
<li>Also select <strong>yes</strong> when it asks about automatically loading the kernel module</li>
<li>Use the right arrow to select the <strong>&lt;Finish&gt;</strong> button</li>
<li>Select <strong>yes</strong> when it asks to reboot</li>
</ol>
<p>After rebooting re-check that the <code>dmesg | grep i2c</code> command shows whether
I2C driver is loaded before proceeding.</p>
<p>Optionally, to improve permformance, increase the I2C baudrate from the default
of 100KHz to 400KHz by altering <code>/boot/config.txt</code> to include:</p>
<pre>dtparam=i2c_arm=on,i2c_baudrate=400000
</pre>
<p>Then reboot.</p>
<p>Then add your user to the i2c group:</p>
<pre>$ sudo adduser pi i2c
</pre>
<p>Install some packages:</p>
<pre>$ sudo apt-get install i2c-tools python-pip
</pre>
<p>Next check that the device is communicating properly (if using a rev.1 board,
use 0 for the bus not 1):</p>
<pre>$ i2cdetect -y 1
<p>

       0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
  00:          -- -- -- -- -- -- -- -- -- -- -- -- --
  10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
  70: -- -- -- -- -- -- 76 --
</pre>
<a name="user-content-installing-the-python-package"></a>
<h2><a id="user-content-installing-the-python-package" class="anchor" aria-hidden="true" href="#installing-the-python-package"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installing the Python Package</h2>
<p>For python2, from the bash prompt, enter:</p>
<pre>$ sudo python setup.py install
</pre>
<p>This will install the Python files in <code>/usr/local/lib/python2.7</code>
making them ready for use in other programs.</p>
<p>Alternatively for python3, type:</p>
<pre>$ sudo python3 setup.py install
</pre>
<a name="user-content-cheeseshop-install"></a>
<h3><a id="user-content-cheeseshop-install" class="anchor" aria-hidden="true" href="#cheeseshop-install"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Cheeseshop install</h3>
<p>Alternatively, a version on PyPi is available, just do:</p>
<pre>$ sudo pip install RPi.bme280
</pre>
<a name="user-content-software-driver-example-usage"></a>
<h2><a id="user-content-software-driver---example-usage" class="anchor" aria-hidden="true" href="#software-driver---example-usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Software Driver - Example Usage</h2>
<p>Once installed, confirm the I2C address (see prerequisites, it will most
likely be 0x76 or 0x77) and port.</p>
<p>Then in a python script or REPL:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> smbus2
<span class="pl-k">import</span> bme280

port <span class="pl-k">=</span> <span class="pl-c1">1</span>
address <span class="pl-k">=</span> <span class="pl-c1"><span class="pl-k">0x</span>76</span>
bus <span class="pl-k">=</span> smbus2.SMBus(port)

calibration_params <span class="pl-k">=</span> bme280.load_calibration_params(bus, address)

<span class="pl-c"><span class="pl-c">#</span> the sample method will take a single reading and return a</span>
<span class="pl-c"><span class="pl-c">#</span> compensated_reading object</span>
data <span class="pl-k">=</span> bme280.sample(bus, address, calibration_params)

<span class="pl-c"><span class="pl-c">#</span> the compensated_reading class has the following attributes</span>
<span class="pl-c1">print</span>(data.id)
<span class="pl-c1">print</span>(data.timestamp)
<span class="pl-c1">print</span>(data.temperature)
<span class="pl-c1">print</span>(data.pressure)
<span class="pl-c1">print</span>(data.humidity)

<span class="pl-c"><span class="pl-c">#</span> there is a handy string representation too</span>
<span class="pl-c1">print</span>(data)</pre></div>
<p>This then should print something like:</p>
<pre>ee50df9c-3aa3-4772-8767-73b6bb74f30f
2016-11-18 17:33:28.937863
20.563
980.91
48.41
compensated_reading(id=ee50df9c-3aa3-4772-8767-73b6bb74f30f,
    timestamp=2016-11-18 17:33:28.937863, temp=20.563 °C,
    pressure=980.91 hPa, humidity=48.41 % rH)
</pre>
<p>For a data-logger like application, periodically call <code>bme2.sample(bus, address, calibration_params)</code> to
get time-based readings.</p>
<p>See the <a href="https://github.com/rm-hull/weatherstation">weatherstation project</a> for
a more complete example usage.</p>
<a name="user-content-references"></a>
<h2><a id="user-content-references" class="anchor" aria-hidden="true" href="#references"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>References</h2>
<p>&gt; TODO</p>
-----------------------------------------------------------------------------
Adafruit_Python_BME280
This Python driver allows you to read data from the Adafruit BME280 Breakout on a Raspberry Pi, Pi2 or similar device.
-------------------------------------------------------------------------------------------------
Requirements
This driver requires that you have previously installed the Adafruit_Python_GPIO package.

On Raspbian, you can install this package with the following commands:



<h2><a id="user-content-requirements" class="anchor" aria-hidden="true" href="#requirements"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Requirements</h2>
<p>This driver requires that you have previously installed the
<a href="https://github.com/adafruit/Adafruit_Python_GPIO">Adafruit_Python_GPIO</a> package.</p>
<p>On Raspbian, you can install this package with the following commands:</p>
<pre><code>sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
</code></pre>
<h2><a id="user-content-usage" class="anchor" aria-hidden="true" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage</h2>
<p>To read a single set of data points from the BME, connect your Pi or Pi2
to the BME280 breakout using I2C (connect SCL0/1 to the SCK pin and SCL0/1
to the SDI pin), and run the following command from this folder:</p>
<pre><code>python Adafruit_BME280_Example.py
</code></pre>




---------------


