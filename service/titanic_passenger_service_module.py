import csv

from models.Passenger import Passenger


class TitanicPassengerService(object):
    CSV_FILE_PATH = "./titanic.csv"

    def __init__(self):
        self.passenger_dict = {}
        self._read_csv_file(self.CSV_FILE_PATH)

    def _read_csv_file(self, path):
        with open(path) as f:
            reader = csv.DictReader(f)
            for line in reader:
                self.passenger_dict[line['PassengerId']] = (Passenger(**line))

    def get_histogram_data(self):
        try:
            return
        except Exception as e:
            raise Exception(e)

    def get_passenger_data(self, passenger_id):
        try:
            passenger = self.passenger_dict.get(passenger_id)
            if passenger:
                return passenger.to_dict()
        except Exception as e:
            raise Exception(e)

    def get_requested_attribute(self, passenger_id, attribute_list):
        try:
            requested_attribute_list = []
            attribute_list = [attribute.lower() for attribute in attribute_list]
            passenger = self.passenger_dict.get(passenger_id)
            if passenger:
                passenger = passenger.to_dict()
                for attribute, value in passenger.items():
                    attribute = attribute.lower()
                    if attribute in attribute_list:
                        requested_attribute_list.append(value)
                return requested_attribute_list
        except Exception as e:
            raise Exception(e)

    def get_all_passengers(self):
        try:
            passengers = list(self.passenger_dict.values())
            passengers_data = [passenger.to_dict() for passenger in passengers]
            return passengers_data
        except Exception as e:
            raise Exception(e)



