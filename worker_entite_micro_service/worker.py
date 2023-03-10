import kafka_consumer 
import mongo_client 
import time
import traceback
from translate import Translator

if __name__ == '__main__':
	kafka_connection = kafka_consumer.create_consumer('topic') 
	mongo_connection = mongo_client.DataAccessMongo()
	translator = Translator (from_lang="french", to_lang="english") 
	while True:
		data_in = kafka_consumer.read_from_topic(kafka_connection) 
		if len(data_in) > 0:
			for elt in data_in:
				try:
					print(elt)
					print(f"Entité id={elt['id']} reçue")
					elt['contenu_entité_anglais'] = translator.translate(elt['contenu_entité']) 
					print(f"Ajout de l'entité id={elt['id']} dans la base de données") 
					mongo_connection.add_entity(elt)
				except Exception:
					print(traceback.format_exc())
		time.sleep(2)