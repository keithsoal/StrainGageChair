# Read strain data from wheatstone bridge with HX711
import RPi.GPIO as GPIO
from hx711 import HX711

def configureStrain():
    try:
        GPIO.setmode(GPIO.BCM)  # GPIO BCM numbering (Broadcom SOC channel)

        hx = HX711(dout_pin=21, pd_sck_pin=20, gain_channel_A=128)
        # Create an object hx which represents your real hx711 chip
        # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
        # If you do not pass any argument 'gain_channel_A' then the default value is 128
        # If you do not pass any argument 'set_channel' then the default value is 'A'
        # you can set a gain for channel A even though you want to currently select channel B

        err = hx.zero()
        if err:  # you can check if the reset was successful
            print('not ready')
        else:
            print('Ready to use')

        # Read data several, or only one, time and return mean value
        # argument "readings" is not required default value is 30
        data = hx.get_raw_data_mean(readings=30)
        if data:  # always check if you get correct value or only False
            print('Raw data:', data)
        else:
            print('invalid data')

        # set scale ratio for particular channel
        ratio = 2.83 # data / value [mV/g]
        hx.set_scale_ratio(ratio)

        return hx

def getStrain(hx):

    # Read data several times and return mean value
    # subtracted by offset and converted by scale ratio to
    # desired units. In my case in grams.
    # while True:
    #     print(hx.get_weight_mean(20))

    strain = hx.get_weight_mean(20)
    return strain

#except (KeyboardInterrupt, SystemExit):
    #print('Bye :)')

    #finally:
        #GPIO.cleanup()
