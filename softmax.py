import numpy as np
import matplotlib.pyplot as plt
import math

w = [1,2,3,4,5,6,7,8,9,10] # Scores
k = [0.01,0.1,1,2,5] # factor
color = ['r','g','b','k','m']
for j in range(len(k)):
    denom = 0
    r = [None]*10
    for wi in w:
        denom = denom + math.exp(k[j]*wi)
    for i in range(len(w)):
        r[i] = math.exp(k[j]*w[i])/denom
    plt.plot(w,r,linewidth=2,label='k='+str(k[j]),color=color[j])
plt.legend()
plt.show()
