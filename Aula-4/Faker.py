#!/usr/bin/python3

from pymongo import  MongoClient
from pprint import pprint
from bson import ObjectId
from faker import Faker
from datetime import datetime
from time import sleep

fake = Faker('pt_BR')

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

# print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
# for x in range (1000):
#     registro = {"nome":fake.name(),
#     "endereço":[{"comercial":fake.address(),"residencial":fake.address()}],
#     "telefone":[{"celular":fake.phone_number(),"residencial":fake.phone_number()}]}
#     db.usuarios.insert(registro)
# print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

for x in db.usuarios.find():
    print(x)
    sleep(1)