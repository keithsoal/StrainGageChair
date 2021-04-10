# Measure strain from wheatstone bridge and temperature from digital temp sensor

from getStrain import getStrain
from getStrain import configureStrain
from getTemp import getTemp
from getTemp import configureTemp
import time
import socket
import numpy as np

# create configuration file
sleeptime = 1

UDP_IP_ADDRESS = "192.168.1.102"
UDP_PORT_NO = 6789

hx = configureStrain()
device_file = configureTemp()

try:
    while True:
        # get data
        strain = getStrain(hx)
        temp = getTemp(device_file)
        print("Strain",strain)
        print("Temperature",temp)
        #time.sleep(sleeptime)

        sys = np.array([strain,temp],dtype=float)
        payload = sys.tobytes()

        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.sendto(payload, (UDP_IP_ADDRESS, UDP_PORT_NO))

except (KeyboardInterrupt, SystemExit):
    print('Bye :)')

finally:
    GPIO.cleanup()
