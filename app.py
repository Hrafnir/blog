from Database import Database
from models.post import Post
from models.Blog import Blog
from menu import Menu


__author__ = 'hraffy'

Database.initializing_main_db()

menu = Menu()
menu.run_menu()







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