"""

this program displays probability


import numpy as np
a = [0.6, 0.4]

b = [[0.7, 0.3], [0.6, 0.4]]
n = int(input("prediction of how many ahead u want: "))
while(n):
    x = np.matmul(a, b)
    a = x
    n-=1
    print(x)
"""