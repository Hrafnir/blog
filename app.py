from Database import Database
from models.post import Post
from models.Blog import Blog

__author__ = 'hraffy'

Database.initializing_main_db()

blog = Blog('Jose', 'Same title', 'Same_sedsafasdv')

blog.save_to_db()
blog.new_post()











#
# import pymongo
#
# uri = 'mongodb://127.0.0.1:27017'
# client = pymongo.MongoClient(uri)
# database = client['blog']
# collection = database['students']
# students = collection.find({})
# valera = collection.find({'age': 21}, {'_id': 0})
# # # student_mark = [i['Mark'] for i in collection.find({}) if i['Mark'] == 23] #выдаст values от keys 'mark'
# # print(student_mark)
# print(valera)
# for i in students:
#     print(i)