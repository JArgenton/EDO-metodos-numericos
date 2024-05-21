import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os
from function import Function as Fx


def achavalores(F:Fx, x: float, y: float, a, b, p, q):
    """funcao qe faz coisas"""
    h = F.h
    K1 = F.derivada(x[-1], y[-1])
    K2= F.derivada(x[-1] + p*h, y[-1] + q*h*F.derivada(x[-1], y[-1]))
    dy = (a*K1 + b*K2)
    return dy

def make_achavalores(F:Fx):
    """d dddd sdsad asdad adaaadd swd dd"""
    a = 0
    while a <= 1:

        b = 1 - a
        q = 0.5/b
        p = q

        x = [F.inicial[0]]
        y = [F.inicial[1]]
        for _ in range(F.n_passos):
            newx = x[-1] + F.h
            newy = achavalores(F, x[-1], y[-1], a, b, p, q)
            x.append(newx)
            y.append(newy)
        a = a + 0.1







intervalo = (0, 5)
Func = Fx(inicial, intervalo, 30)