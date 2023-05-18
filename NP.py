import numpy as np
def alg1():
    x = np.arange(25, dtype=np.int16).reshape(5, 5)
    print(x)
    print(x+3)
def alg2():
    d = np.random.randint(3, 2)
    print(d)
alg1()