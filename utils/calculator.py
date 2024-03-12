import json
from datetime import datetime
import csv


class RamatCalculator:
    def __init__(self, name, age, start_serving_date, end_service_date):
        self.name = name
        self.age = age
        self.start_serving_date = datetime.strptime(start_serving_date, "%d/%m/%Y")
        self.end_service_date = datetime.strptime(end_service_date, "%d/%m/%Y")

    def serving_time(self):
        serving_time = self.end_service_date - self.start_serving_date
        return serving_time

    def to_json(self):
        return {"Name": self.name,
                "Age": self.age,
                "Start_date": str(self.start_serving_date),
                "End_date": str(self.end_service_date)}
