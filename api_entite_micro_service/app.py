from flask import Flask, request
from flask_restx import Api, Resource, fields
import kafka_producer

app = Flask(__name__)
api = Api(app, version='0.1', title='API Python', description="Cette API permet d'ajouter une entité.")

namespace_entity = api.namespace('entite', description="Contient une liste d'opérations sur les entités.")
entity_model = api.model('Entité', {
	'id': fields. Integer (readonly=True, description="Identifiant unique de l'entité", example=1),
	'libelle_entité': fields.String(required=True, description="Le libellé de l'entité", example='Ma LUBULULE'), 
	'contenu_entité': fields.String(required=True, description="Le conteny de l'entité", example='Mon contenu')
})

@namespace_entity.route('/<int:id>')
class EntityIdQueries(Resource):
	@namespace_entity.doc('Ajouter une nouvelle entité')
	@namespace_entity.expect(entity_model)
	@namespace_entity.response (201, 'Success') 
	@namespace_entity.response (400, 'Fail')
	def post(self, id):
		print(f"Réception d'une requête d'ajout d'entité id={id}")
		if 'libelle_entité' not in api.payload or api.payload['libellé_entité'] == "":
			return "Libellé non trouvé ou vide", 400
		if 'contenu_entité' not in api.payload or api.payload['contenu_entité'] == "":
			return "contenu non trouvé ou vide", 400

		api.payload['id'] = id 
		uccess = True
		print(f"Mettre l'entité dans le topic id={id}") 
		success = kafka_producer.put_in_topic(api.payload) 
		if success:
			return f"L'entité a été ajoutée", 201
		else:
			return f"L'entité n'a pas été ajoutée", 400