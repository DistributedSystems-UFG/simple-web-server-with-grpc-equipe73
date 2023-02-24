from concurrent import futures
import logging

import grpc
import SensorService_pb2
import SensorService_pb2_grpc

empDB=[
 {
 'date':'11/11/21',
 'location':'living room',
 'value':11.3
 }]

class SensorServer(SensorService_pb2_grpc.SensorServiceServicer):

  def CreateSensor(self, request, context):
    dat = {
    'date':request.date,
    'location':request.location,
    'value':request.value
    }
    empDB.append(dat)
    return SensorService_pb2.StatusReply(status='OK')

  def GetSensorDataFromdate(self, request, context):
    usr = [ emp for emp in empDB if (emp['date'] == request.date) ] 
    list = SensorService_pb2.SensorDataList()
    for item in usr:
      emp_data = SensorService_pb2.SensorData(date=item['date'], location=item['location'], value=item['value']) 
      list.Sensor_data.append(emp_data)
    return list
    
  def GetSensorDataFromlocation(self, request, context):
    usr = [ emp for emp in empDB if (emp['location'] == request.location) ] 
    list = SensorService_pb2.SensorDataList()
    for item in usr:
      emp_data = SensorService_pb2.SensorData(date=item['date'], location=item['location'], value=item['value']) 
      list.Sensor_data.append(emp_data)
    return list

  def ListAllSensors(self, request, context):
    list = SensorService_pb2.SensorDataList()
    for item in empDB:
      emp_data = SensorService_pb2.SensorData(date=item['date'], location=item['location'], value=item['value']) 
      list.Sensor_data.append(emp_data)
    return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SensorService_pb2_grpc.add_SensorServiceServicer_to_server(SensorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()