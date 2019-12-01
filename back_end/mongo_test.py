
from flask_restplus import Resource
from flask_restplus import Api
from flask import make_response, session, jsonify
from pymongo import MongoClient


apiMongo = Api(version='1.0', title='API Mongo',description='Beta version of docker API')
nsMongo= apiMongo.namespace('default', description='Operations related to Mongo connection')

@nsMongo.route('/mongoconnection')
class mongo(Resource):
    def get(self):
        #second mongodb must match the docker-compose file name
        client = MongoClient("mongodb://mongodb:27017")

        ##WARNING IF data was not persisted (with docker volumes), after creating the container, db1 and collection "people" need to be created firsr !
        db = client.db1
        collection = db.people
        return list(collection.find({},{"_id":0}))



