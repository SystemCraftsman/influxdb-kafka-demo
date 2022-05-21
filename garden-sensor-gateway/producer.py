import time

from kafka import KafkaProducer

def main():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    csv_data_file = open('../resources/data/garden-sensor-data.json', 'r')
    lines = csv_data_file.readlines()

    for line in lines:
        producer.send('garden_sensor_data', bytes(f'{line}','UTF-8'))
        print(f"Sensor data is sent: {line}")
        time.sleep(5)

if __name__ == "__main__":
    main()
