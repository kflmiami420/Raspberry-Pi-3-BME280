# import libraries

import math
import bme280
from twython import Twython
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

    while: yes
        twitter_status = get_timestamp() + " - Update - " + reasonf
        twitter.update_status(status=twitter_status)

    except:
        print("Failed to send tweet")


     while : no
            twitter_status = get_timestamp() + " - Temperature : " + str(temperature) + "F / Temperature 2:" + str(temperature2) + "C / Pressure: " + str(pascals) + "hPa"
            log("Attempting to tweet - " + twitter_status)
            twitter.update_status(status=twitter_status)

        except:
            print("Twython did not tweet")
            log("Twython did not tweet")

#        print("Sleeping for 15 minutes")
#        sleep(900)

# Twitter detects repetition, so timestamp the tweets to prevent them reading as duplicates
#def get_timestamp():
#    timestamp = strftime("%Y%m%d-%H:%M:%S")

#    return timestamp


#!/usr/bin/env python
import os
from twython import Twython


CONSUMER_KEY = 'H2OaDt1XW52JsmFrlPOzr6EbA'
CONSUMER_SECRET = 'F7slLnT5ovKMowFLhSsrhhTM8kErWpLDrGngwahizaDRtNXrgR'
ACCESS_KEY = '1017199136121217026-fX37Uf2m7hXcuLnD9ekdFCrL1znxdz'
ACCESS_SECRET = 'Op1lMH6sS6GRYMaRmeyGlCvKmc0sXKCWDz9ezNS4NySwe'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My CPU temperature is '+temp+' C')
print (sleeping for 15 minutes)
sleep 900

