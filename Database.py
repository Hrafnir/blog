import pymongo

__author__ = 'hraffy'


class Database:
    uri = 'mongodb://127.0.0.1:27017'
    database = None

    @staticmethod
    def initializing_main_db():
        clinet = pymongo.MongoClient(Database.uri)
        Database.database = clinet ['blog']

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)
        return 'Data posted!'

    @staticmethod
    def find(collection, query):
        return Database.database[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)