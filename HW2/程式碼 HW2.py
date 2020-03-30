import numpy as np
import pandas as pd
import math
bp = int(input('The Bond Price: '))
fv = int(input('The Face Value: '))
cr = int(input('The Coupon Rate(%): '))
y = int(input('Years to Maturity: '))
pay = int(input('Payment:annually(1)/semi-annually(2)/quarterly(4). Please insert the number: '))
coupon = fv * (cr/pay) * 0.01

YTM = [0] * y * pay
spot_rate = [0] * y * pay
pv = 0
for i in range(y*pay):
    cash_flow = [bp*-1] + [coupon]*(i) + [coupon + fv]
    YTM[i] = np.irr(cash_flow)
    if i <= pay-1 :
        spot_rate[i] = YTM[i]
    else:
        pv += coupon / (1 + spot_rate[i-1])**i
        x = (fv + coupon) / (bp - pv)
        spot_rate[i] = math.pow(x, 1/(i+1)) - 1


forward_rate = [[0]*y*pay for i in range(y*pay)]
for i in range(y*pay):
    for j in range(y*pay):
        z = ((1+spot_rate[j])**j)/((1+spot_rate[i])**i)
        if j-i == 0:
            forward_rate[i][j] = 0
        else:
            forward_rate[i][j] = z**(1/(j-i)) - 1

table = pd.DataFrame(forward_rate)   
#print(YTM)
#print(spot_rate)
print(table)
