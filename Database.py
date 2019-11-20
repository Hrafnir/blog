import pymongo

__author__ = 'hraffy'


class Database:
    uri = 'mongodb://127.0.0.1:27017'
    db = None

    @staticmethod
    def initializing_main_db():
        client = pymongo.MongoClient(Database.uri)
        Database.db = client['blog']

    @staticmethod
    def insert(collection, data):
        Database.db[collection].insert(data)
        return 'Data posted!'

    @staticmethod
    def find(collection, query):
        return Database.db[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.db[collection].find_one(query)