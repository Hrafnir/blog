__author__ = 'hraffy'

import pymongo

uri = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(uri)
database = client['blog']
collection = database['students']
students = collection.find({})
student_mark = [i['Mark'] for i in collection.find({}) if i['Mark'] == 23] #выдаст values от keys 'mark'
print(student_mark)
for i in students:
    print(i)


