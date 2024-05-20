import matplotlib.pyplot as plt
import numpy as np
import funçao as f

# Yk+1 = Yk + h(y'(x+h/2, y + h/2y1(x, y)))
#y'k = -y + t +1 

# para melhor entedimento, usarei t no lugar de x, representando a funçao no tempo. 


def Euler_ponto_medio(coord_inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos):

    passo = ((intervalo[1] - intervalo[0]) / n_passos)
    x_values = [coord_inicial[0]]
    y_values = [coord_inicial[1]]

    for _ in range(n_passos):
        x = x_values[-1]
        y = y_values[-1]

        k1 = f.derivada_funçao(x, y)

        k2 = f.derivada_funçao(x + passo / 2, y + (passo / 2) * k1)
   
        newy = y + passo * k2
       

        x_values.append(x + passo)
        y_values.append(newy)

    return x_values, y_values


 
    


        