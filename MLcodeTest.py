# this is a little bit of Python code from another project I started, just using this as a test

import random

# Represents the properties of the environment
class Environment (object):
    
    # Initializes all environmental factors: temperature, disease, cold, and hot
    def __init__(self, temperature, disease):
        # self.temperature = random(50, 90)
        # self.disease = random(0, 10)
        self.temperature = temperature
        self.disease = disease
        if self.temperature < 70:
            self.cold = (70 - self.temperature) / 2
            self.hot = 0
        elif self.temperature > 70:
            self.cold = 0
            self.hot = (self.temperature -  70) / 2
        else:
            self.cold = 0
            self.hot = 0

    def initializeEnvironment():
        temperature = random(50, 90)
        disease = random(0, 10)
        environment = Environment(temperature, disease)
        return environment
