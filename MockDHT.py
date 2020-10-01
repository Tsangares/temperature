import random
class MockDHT:
    def __init__(self):
        self._temperature=0
        self._humidity=0
    def measure(self):
        self._temperature = random.random()*100
        self._humidity = random.random()*100

    @property
    def temperature(self):
        self.measure()
        return int(self._temperature)

    @property
    def humidity(self):
        self.measure()
        return int(self._humidity)
