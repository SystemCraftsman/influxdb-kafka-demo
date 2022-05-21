import random
import json


def random_temp_cels():
    return round(random.uniform(-10, 50), 1)

def random_humidity():
    return round(random.uniform(0, 100), 1)

def random_wind():
    return round(random.uniform(0, 10), 1)

def random_soil():
    return round(random.uniform(0, 100), 1)

def get_json_data():
    data = {}

    data["temperature"] = random_temp_cels()
    data["humidity"] = random_humidity()
    data["wind"] = random_wind()
    data["soil"] = random_soil()

    return json.dumps(data) 

file_object = open('garden-sensor-data.json', 'a')

for i in range(20000):
    json_data = get_json_data()
    file_object.write(f"{json_data}\n")
    print(json_data)

file_object.close()
