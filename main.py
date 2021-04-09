# Measure strain from wheatstone bridge and temperature from digital temp sensor

from getStrain import getStrain
from getTemp import getTemp
from time import sleep

# create configuration file

hx = configureStrain()
device_file = configureTemp()

while True:
    # get data
    strain = getStrain(hx)
    temp = getTemp(device_file)
    time.sleep(sleeptime)

    # write to inlfuxDB

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

        finally:
            GPIO.cleanup()
