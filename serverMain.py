import socket
import logging
import numpy as np
from influxdb import InfluxDBClient
import uuid
import random
import time

# socket configuration
UDP_IP_ADDRESS = "192.168.1.104" #"192.168.137.1"
UDP_PORT_NO = 6789

# influxDB configuration
client = InfluxDBClient(host='localhost', port=8086)
client.create_database('StrainGageChair')
measurement_name = 'Prototype'
id_tags = ['ad0f4889-fa27-4f6a-b20b-eda0bd0c0828']

# debug
logging.basicConfig(level=logging.DEBUG)

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))

while True:
    payload, add = serverSock.recvfrom(1024)
    print("Message: ", payload)

    array = np.frombuffer(payload)
    logging.debug("Payload: {}".format(array))

    data = []
    data.append("{measurement},id={id} strain={strain},temp={temp}"
                .format(measurement=measurement_name,
                        id=random.choice(id_tags),
                        strain=array[0],
                        temp=array[1]))

    client.write_points(data, database='StrainGageChair', time_precision='ms', batch_size=10, protocol='line')
    #time.sleep(1)
