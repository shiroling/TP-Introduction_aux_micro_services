from pymongo import MongoClient

database_host = 'database' 
database_port = 27017

class DataAccessMongo(object):
	def __init__(self):
		self.client = MongoClient(database_host, database_port) 
		self.db = self.client['DB']
		self.collection_entite = self.db['Entite']

	def add_entity(self, entity):
		self.collection_entite.insert_one(entity)