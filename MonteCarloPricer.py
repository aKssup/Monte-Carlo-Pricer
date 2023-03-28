from GeometricBrownianMotionPricer import GeometricBrownianMotion
# from BlackScholesPricer import BlackScholesPricerCall
# from BlackScholesPricer import BlackScholesPricerPut
import matplotlib.pyplot as plt
import numpy as np

class MonteCarloPricer:
    
    def __init__(self, strike):
        self.strike = strike

    def getPayoff(self, stockPrice):
        if stockPrice > self.strike:
            return stockPrice - self.strike
        else:
            return 0

    @staticmethod
    def main():
        pricePaths = GeometricBrownianMotion.main()
        callPayoffs = []
        eObj = MonteCarloPricer(100)
        riskFreeRate = 0.01
        for p in pricePaths:
            # Getting the last stock price to determine payoff and discount it by one year
            callPayoffs.append(eObj.getPayoff(p[-1]) / (1 + riskFreeRate))

        for p in pricePaths:
            plt.plot(p) 
        
        # plt.show()

        # Options are in blocks on 100
        print(np.average(callPayoffs) * 100)

# Monte Carlo Price of an European Call Option
MonteCarloPricer.main()
