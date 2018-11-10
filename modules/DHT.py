import Adafruit_DHT
import threading, time

SENSOR_MODEL = 11
READING_FREQ = 30

class DHT(threading.Thread):
    def __init__(self, pin, sensor_model = SENSOR_MODEL):
        threading.Thread.__init__(self)
        self.pin = pin
        self.sensor_model = sensor_model
        self.temperature = None
        self.humidity = None
        self.time = None
        self.isStopped = threading.Event()

    def run(self):
        while not self.isStopped.is_set():
            self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor_model, self.pin)
            self.time = time.time()
            self.isStopped.wait(READING_FREQ)

    def stop(self):
        self.isStopped.set()

    def getReading(self):
        return (self.temperature, self.humidity, self.time)

