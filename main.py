# Measure strain from wheatstone bridge and temperature from digital temp sensor

from getStrain import getStrain
from getTemp import getTemp

# create configuration file

while True:
    # get data
    strain = getStrain()
    temp = getTemp()
    
    # write to inlfuxDB