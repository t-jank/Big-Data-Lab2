# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:10:00 2023

@author: t-jan
"""
import random
import yfinance as yf
import matplotlib.pyplot as plt


def Vitters_algorithm_R(k,x):
    R=[]
    n=len(x)
    for i in range(0,k):
        R.append(x[i])
    for i in range(k,n):
        r=random.randint(0,i-1)
        if r<k:
            R.remove(R[r]) # modyfikacja, żeby po kolei; próby niezależne, tak że chyba ok
            R.append(x[i]) # jw
            #R[r]=x[i] # to oryginalnie było
    return R

# takie sprawdzenie
#print(Vitters_algorithm_R(3, [0,1,2,3,4,5,6,7,8,9,10])) 


msft = yf.Ticker("BTC-USD")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="5y")

# get notowania otwarcia
open_markings=hist.Open 

# get losowa próbka 40 elementów
sample=Vitters_algorithm_R(40,open_markings)

xaxis_all=[]
xaxis_sample=[]
for i in range(0,len(open_markings)):
    xaxis_all.append(i)
for i in range(0,len(sample)):
    xaxis_sample.append(i)
plt.plot(xaxis_all,open_markings)
plt.ylabel("Notowanie otwarcia BTC-USD")
plt.xlabel("Liczba dni od 09.06.2018")
plt.title("Wszysktie dzienne notowania otwarcia bitcoina z ostatnich 5 lat")
plt.show()
plt.plot(xaxis_sample,sample)
plt.ylabel("Notowanie otwarcia BTC-USD")
plt.title("Losowa próbka 40 elementów")
plt.show()
