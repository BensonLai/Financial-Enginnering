from scipy.stats import norm
import math

s = float(input('current stock price: '))
x = int(input('strike price: '))
sigma = float(input('variation: '))
div1 = int(input('dividend amount: '))
div1_mon = int(input('ex-dividend month: '))
div2 = int(input('dividend amount: '))
div2_mon = int(input('ex-dividend month: '))
r = float(input('riskless interest rate(%): '))/100
T = float(input('mature period: '))
#R = math.exp(r)

D = div1*math.exp(-r*(div1_mon/12)) + div2*math.exp(-r*(div2_mon/12))
s_hat = s - D
d1 = (math.log(s_hat/x) + (r+sigma**2/2)*(T/12)) / (sigma * (T/12)**0.5)
d2 = d1 - sigma * (T/12)**0.5
p = x*math.exp(-r*(T/12))*norm.cdf(-d2) - s_hat*norm.cdf(-d1)

print('The option price is:', p)


