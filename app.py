from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from routes import titanic_passenger_controller

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Titanic-passengers-Flask-REST"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(titanic_passenger_controller.get_blueprint())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
