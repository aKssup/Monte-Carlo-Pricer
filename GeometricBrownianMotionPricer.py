import matplotlib.pyplot as plt
import numpy as np
import math

class GeometricBrownianMotion:

    def __init__(self, initialPrice, drift, volatility, dt, T):
        self.currentPrice = initialPrice
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.prices = []
        self.simulatePaths()

    def simulatePaths(self):
        while(self.T - self.dt > 0):
            dWt = np.random.normal(0, math.sqrt(self.dt)) # Brownian Motion
            dYt = self.drift * self.dt + self.volatility * dWt
            self.currentPrice += dYt
            self.prices.append(self.currentPrice)
            self.T -= self.dt

    @staticmethod
    def main():
        # Can play around with set and input parameters i.e. modify
        # Set Parameters
        drift = 0.08
        volatility = 0.1
        dt = 1/365
        T = 1
        pricePaths = []

        # Input Parameters
        # print("Put in your initial price.")
        initialPrice = 100
        # print("Put in your desired number of paths.")
        paths = 100

        for i in range(0, paths):
            pricePaths.append(GeometricBrownianMotion(initialPrice, drift, volatility, dt, T).prices)

        return pricePaths

pricePaths = GeometricBrownianMotion.main()

for p in pricePaths:
    plt.plot(p)

# plt.show()