import random
import datetime
from faker import Faker
fake = Faker('en_US')
Faker.seed(0)

def generateFakeData(count = 1000, deviceCount = 10):
  devices = createDevices(deviceCount)
  sensors = [
    { 'name': 'variacaoTemperatura', 'lower': -1, 'upper': 1 },
    { 'name': 'vibracao', 'lower': 0, 'upper': 1 },
    { 'name': 'rotacao', 'lower': 0, 'upper': 1 }
  ]
  data = []
  i = 0
  while i < count:
    data.append(createRandomData(devices, sensors))
    i += 1
  return data

def createDevices(count):
  return list(map(lambda n: f'caixa {n}', list(range(1, count + 1))))

def createRandomData(devices, sensors):
  (latitude, longitude, rua, pais, continente) = fake.local_latlng()
  data = {
      'caixa': random.choice(devices),
      'dataHora': nowUtc(),
      'posicao': {
        'latitude': latitude,
        'longitude': longitude,
        'rua': rua,
        'pais': pais,
        'continente': continente
      }
  }
  for sensor in sensors:
    data[sensor['name']] = random.randint(sensor['lower'], sensor['upper'])
  return data

def nowUtc():
  return datetime.datetime.now(datetime.timezone.utc).strftime("%m/%d/%Y, %H:%M:%S:%f")