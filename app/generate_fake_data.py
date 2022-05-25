import random
import datetime

def generateFakeData(count = 1000, deviceCount = 10):
  devices = createDevices(deviceCount)
  sensors = ['flow', 'temperature', 'sound', 'humidity']
  data = []
  id = 0
  while id < count:
    data.append(read(devices, sensors))
    id += 1
  return data

def createDevices(count):
  return list(map(lambda n: f'device {n}', list(range(1, count + 1))))

def read(devices, sensors):
  return {
      'device': random.choice(devices),
      'sensor': random.choice(sensors),
      'value': random.randint(50, 400),
      'time': nowUtc()
  }

def nowUtc():
  return datetime.datetime.now(datetime.timezone.utc).strftime("%m/%d/%Y, %H:%M:%S:%f")