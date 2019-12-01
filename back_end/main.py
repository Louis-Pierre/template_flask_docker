
from flask import Flask, Blueprint
from flask_restplus import Api
from statusCheck import apiStatus, nsCheck
from mongo_test import apiMongo, nsMongo


app = Flask(__name__)
blueprint = Blueprint('api-test', __name__, url_prefix='/api-test')
blueprint2 = Blueprint('mongo-test', __name__, url_prefix='/mongo-test')

apiStatus.init_app(blueprint)
apiStatus.add_namespace(nsCheck)
app.register_blueprint(blueprint)

apiMongo.init_app(blueprint2)
apiMongo.add_namespace(nsMongo)
app.register_blueprint(blueprint2)


@app.route("/")
def hello():
    return "It's fucking working !!!"



if __name__ == "__main__":
    app.run(debug=True)