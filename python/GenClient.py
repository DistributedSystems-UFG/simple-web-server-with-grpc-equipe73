from __future__ import print_function
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc
import random
import const
dates = ['11/11/2021', '01/10/2016', '12/12/2012', '05/05/2005', '06/05/2005', '07/05/2005', '08/05/2005', '10/05/2005']
locations = ['room 1', 'room 2', 'kitchen', ' living room', 'bathroom', 'garden', 'garage', 'basement',]
def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = SensorService_pb2_grpc.SensorServiceStub(channel)

        # Add a new Sensor
        response = stub.CreateSensor(SensorService_pb2.SensorData(date=random.choice(dates), location=random.choice(locations), value=random.random()))
        print ('Added new Sensor ' + response.status)

        # List all Sensors
        response = stub.ListAllSensors(SensorService_pb2.EmptyMessage())
        print ('All Sensors: ' + str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()