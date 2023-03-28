from scipy.stats import norm
import math

class BlackScholesPricerCall:
    
    def __init__(self, assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate):
        self.assetPrice = assetPrice
        self.assetVolatility = assetVolatility
        self.strikePrice = strikePrice
        self.timeToExpiration = timeToExpiration
        self.riskFreeRate = riskFreeRate
        self.price = self.callPrice(assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate)

    def callPrice(self, assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate):
        b = math.exp(-riskFreeRate * timeToExpiration)

        x_1 = math.log(assetPrice / (b * strikePrice)) + 0.5 * (assetVolatility * assetVolatility) * timeToExpiration
        x_1 = x_1 / (assetVolatility * (timeToExpiration ** 0.5))
        z_1 = norm.cdf(x_1)
        z_1 = z_1 * assetPrice

        x_2 = math.log(assetPrice / (b * strikePrice)) - 0.5 * (assetVolatility * assetVolatility) * timeToExpiration
        x_2 = x_2 / (assetVolatility * (timeToExpiration ** 0.5))
        z_2 = norm.cdf(x_2)
        z_2 = z_2 * b * strikePrice

        return z_1 - z_2

class BlackScholesPricerPut:

    def __init__(self, assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate):
        self.assetPrice = assetPrice
        self.assetVolatility = assetVolatility
        self.strikePrice = strikePrice
        self.timeToExpiration = timeToExpiration
        self.riskFreeRate = riskFreeRate
        self.price = self.putPrice(assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate)

    def putPrice(self, assetPrice, assetVolatility, strikePrice, timeToExpiration, riskFreeRate):
        b = math.exp(-1 * (riskFreeRate) * timeToExpiration)
        x_1 = math.log((b * strikePrice) / assetPrice) + 0.5 * (assetVolatility * assetVolatility) * timeToExpiration
        x_1 = x_1 / (assetVolatility * (timeToExpiration ** 0.5))
        z_1 = norm.cdf(x_1)
        z_1 = z_1 * b * strikePrice

        x_2 = math.log((b * strikePrice) / assetPrice) + 0.5 * (assetVolatility * assetVolatility) * timeToExpiration
        x_2 = x_2 / (assetVolatility * (timeToExpiration ** 0.5))
        z_2 = norm.cdf(x_2)
        z_2 = z_2 * assetPrice
        
        return z_1 - z_2

eObj = BlackScholesPricerCall(100, 0.3, 100, 1, 0.01)
print(eObj.price)
