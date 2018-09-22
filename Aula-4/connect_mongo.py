#!/usr/bin/python3

from pymongo import  MongoClient
from pprint import pprint
from bson import ObjectId

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

# ling = {'daniel':'python','hector':'php','joao':'javascript'}

# db.teste.insert(ling)
# pprint(db.usuario.find_one())

# for x in db.usuario.find():
#     print(x)
print([x for x in db.usuario.find()])
# db.usuario.insert({"_id":4,"nome":"josé"})
# db.usuario.remove({"_id":4})

db.usuario.remove({'_id': ObjectId('5ba63bb190b30cf3183f6f0d')})
# para trabalhar com ObjectId precisamos importar o bson (ObjectId)