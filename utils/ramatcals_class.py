import csv
import json

from calculator import RamatCalculator
class ramatcals(RamatCalculator):
    def __init__(self, name, age, start_serving_date, end_serving_date):
        super().__init__(name, age, start_serving_date, end_serving_date)

    def RAMATCAL_to_csv(self, filename):
        try:
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(['Name', 'Age', 'Start Serving Date', 'End Serving Date'])
                writer.writerow([self.name, self.age, self.start_serving_date, self.end_service_date])
        except FileNotFoundError:
            print(f"File {filename} not found.")
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Age', 'Start Serving Date', 'End Serving Date'])
                writer.writerow([self.name, self.age, self.start_serving_date, self.end_service_date])
        except Exception as e:
            print(f"Error occurred: {e}")
    def ramatcals_to_json(self,filename,jsonobject):
        with open(filename, 'r') as file:
            data = json.load(file)

        data.append(jsonobject)

        with open('jsonfile', 'w') as file:
            json.dump(data,file)

