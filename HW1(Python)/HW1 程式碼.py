import pandas as pd
import math
x = int(input('請輸入本金: '))
y = int(input('請輸入年數: '))
r = float(input('請輸入年利率(%): '))
c = math.ceil(x/y/12)
listc = [c]*y*12
listc[y*12-1] = x - c*(y*12-1)
listr = [0]*y*12
listt = [0]*y*12
ind = [0]*y*12
for i in range(y*12):
    listr[i] = (x-c*i) * r*0.01/12
    if listr[i] - int(listr[i])<= 0.4:
        listr[i] = int(listr[i])
    else:
        listr[i] = int(listr[i])+1
    listt[i] += listr[i] + listc[i] + listt[i-1]
    ind[i] = str('第'+str(i+1)+'期')
c1 = pd.DataFrame(listc, columns=["本金(元)"], index=ind)
c2 = pd.DataFrame(listr, columns=["利息(元)"], index=ind)
c3 = pd.DataFrame(listt, columns=["本金利息累計(元)"], index=ind)
df = pd.concat([c1,c2,c3], axis=1)
print(df)