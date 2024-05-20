import matplotlib.pyplot as plt
import numpy as np
import funçao as f
import math

# Y = t - e^-t
#y'k = -y + t +1 

# para melhor entedimento, usarei t no lugar de x, representando a funçao no tempo. 



def func_Original(coord_inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos):

    passo = ((intervalo[1] - intervalo[0])/ n_passos)
    x_values = [coord_inicial[0]]
    y_values = [coord_inicial[1]]
    for foo in range(n_passos):

        newx = x_values[-1] + passo

        newy = newx - math.e**-newx

        x_values.append(newx)
        y_values.append(newy)
        
    return x_values, y_values

 
    


        