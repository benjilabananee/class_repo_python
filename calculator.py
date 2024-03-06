from datetime import datetime
import csv
import json

class RamatCalculator:
    def __init__(self, name, age, start_serving_date, end_service_date):
        self.name = name
        self.age = age
        self.start_serving_date = datetime.strptime(start_serving_date, "%Y-%m-%d")
        self.end_service_date = datetime.strptime(end_service_date, "%Y-%m-%d")

    def serving_time(self):
        serving_time = self.end_service_date - self.start_serving_date
        return serving_time

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
                writer.writerow([self.name, self.age, self.start_serving_date, self.end_serving_date])
        except Exception as e:
            print(f"Error occurred: {e}")