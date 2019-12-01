
from flask import Flask, Blueprint
from flask_restplus import Api
from statusCheck import apiStatus, nsCheck


app = Flask(__name__)
blueprint = Blueprint('api-test', __name__, url_prefix='/api-test')

apiStatus.init_app(blueprint)
apiStatus.add_namespace(nsCheck)
app.register_blueprint(blueprint)


@app.route("/")
def hello():
    return "It's fucking working !!!"



if __name__ == "__main__":
    app.run()