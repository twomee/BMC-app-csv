import json
import requests


class CodeExample(object):
    GET_HISTOGRAM_DATA_ENDPOINT = "http://127.0.0.1:5000/get_histogram"
    GET_PASSENGER_DATA_ENDPOINT = "http://127.0.0.1:5000/get_passenger_data"
    GET_REQUESTED_ATTRIBUTE_ENDPOINT = "http://127.0.0.1:5000/get_requested_attribute"
    GET_ALL_PASSENGERS_ENDPOINT = "http://127.0.0.1:5000/get_all_passengers"
    CONT_TYPE = 'application/json; charset=utf-8'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'

    HEADERS = {
        "User-Agent": USER_AGENT,
        "Content-Type": CONT_TYPE,
        "Accept": USER_AGENT,
    }

    def send_get_histogram_data_request(self):
        response = requests.get(self.GET_HISTOGRAM_DATA_ENDPOINT)
        return response

    def send_get_passenger_data_request(self, passenger_id):
        parameters = {"passengerId": f"{passenger_id}"}
        response = requests.get(self.GET_PASSENGER_DATA_ENDPOINT, params=parameters)
        return response

    def send_get_requested_attribute_request(self, passenger_id, attribute_list):
        json_data = {"passengerId": passenger_id, "attributeList": attribute_list}
        response = requests.post(self.GET_REQUESTED_ATTRIBUTE_ENDPOINT, data=json.dumps(json_data), headers=self.HEADERS)
        return response

    def get_all_passengers_request(self):
        response = requests.get(self.GET_ALL_PASSENGERS_ENDPOINT)
        return response

    def get_histogram_data_example(self):
        response = self.send_get_histogram_data_request()
        print(json.loads(response.content))

    def get_passenger_data_example(self):
        passenger_id = 1
        response = self.send_get_passenger_data_request(passenger_id)
        print(json.loads(response.content))

    def get_requested_attribute_example(self):
        passenger_id = 1
        requested_list = ["name", "sex"]
        response = self.send_get_requested_attribute_request(passenger_id, requested_list)
        print(json.loads(response.content))

    def get_all_passengers_example(self):
        response = self.get_all_passengers_request()
        print(json.loads(response.content))


code_example = CodeExample()
code_example.get_histogram_data_example()
code_example.get_passenger_data_example()
code_example.get_requested_attribute_example()
code_example.get_all_passengers_example()
