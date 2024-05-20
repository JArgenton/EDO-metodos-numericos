import matplotlib.pyplot as plt
import numpy as np
import funçao as f

# Yk+1 = Yk + hy'k
#y'k = -y + t +1 

# para melhor entedimento, usarei t no lugar de x, representando a funçao no tempo. 



def Euler(coord_inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos):

    passo = ((intervalo[1] - intervalo[0])/ n_passos)
    x_values = [coord_inicial[0]]
    y_values = [coord_inicial[1]]
    for foo in range(n_passos):
        newx = x_values[-1] + passo
        newy = y_values[-1] + passo * f.derivada_funçao(x_values[-1], y_values[-1])
        x_values.append(newx)
        y_values.append(newy)

    return (x_values, y_values)



        