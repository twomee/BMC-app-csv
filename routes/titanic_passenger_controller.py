import json
from service.titanic_passenger_service_module import TitanicPassengerService
from flask import request, Blueprint

service = TitanicPassengerService()
REQUEST_API = Blueprint('titanic_passenger_controller', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/get_histogram', methods=['GET'])
def get_histogram():
    try:
        histogram_data = service.get_histogram_data()
        return json.dumps({'result': histogram_data}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'status': "fail ==>" + f" {e}"}), 404, {'ContentType': 'application/json'}


@REQUEST_API.route('/get_passenger_data', methods=['GET'])
def get_passenger_data():
    try:
        passenger_id = str(request.args.get('passengerId'))
        passenger_data = service.get_passenger_data(passenger_id)
        return json.dumps({'result': passenger_data}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'result': "fail ==>" + f" {e}"}), 404, {'ContentType': 'application/json'}


@REQUEST_API.route('/get_requested_attribute', methods=['POST'])
def get_requested_attribute():
    try:
        content = request.get_json()
        passenger_id = str(content.get("passengerId"))
        attribute_list = content.get("attributeList")
        requested_attribute_list = service.get_requested_attribute(passenger_id, attribute_list)
        return json.dumps({'result': requested_attribute_list}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'result': "fail ==>" + f" {e}"}), 404, {'ContentType': 'application/json'}


@REQUEST_API.route('/get_all_passengers', methods=['GET'])
def get_all_passengers():
    try:
        passengers = service.get_all_passengers()
        return json.dumps({'result': passengers}), 200, {'ContentType': 'application/json'}
    except Exception as e:
        return json.dumps({'result': "fail ==>" + f" {e}"}), 404, {'ContentType': 'application/json'}
