import matplotlib.pyplot as plt
import numpy as np
import funçao as f

# Yk+1 = Yk + h/2(y'(x, y) + y'(x, y*))
#y'k = -y + t +1 
#y* = Yk + hy'

# para melhor entedimento, usarei t no lugar de x, representando a funçao no tempo. 



def Euler_Melhorado(coord_inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos):

    passo = (intervalo[1] - intervalo[0]) / n_passos
    x_values = [coord_inicial[0]]
    y_values = [coord_inicial[1]]

    for _ in range(n_passos):
        x = x_values[-1]
        y = y_values[-1]

        k1 = f.derivada_funçao(x, y)
     
        k2 = f.derivada_funçao(x + passo, y + passo * k1)
    
        newy = y + (passo / 2) * (k1 + k2)
    

        x_values.append(x + passo)
        y_values.append(newy)

    return x_values, y_values

    


        