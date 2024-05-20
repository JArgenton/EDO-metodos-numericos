import Euler
import Euler_melhorado
import Euler_ponto_medio
import Original
import matplotlib.pyplot as plt
import numpy as np

# PVI
inicial = (1, 0)
intervalo = (0, 5)
# n_interaçoes
passos = 100000


# Obtendo valores de cada metodo
Xval_Euler, Yval_Euler= Euler.Euler(inicial, intervalo, passos)
Xval_Euler_M, Yval_Euler_M= Euler_melhorado.Euler_Melhorado(inicial, intervalo, passos)
Xval_Euler_PM, Yval_Euler_PM = Euler_ponto_medio.Euler_ponto_medio(inicial, intervalo, passos)
Xval_Original, Yval_original = Original.func_Original(inicial, intervalo, passos)

# cria um plano
plt.figure("Métodos Numéricos", figsize=(8, 6))

# plota grafico Euler
plt.plot(Xval_Euler, Yval_Euler, label='Método de Euler', linestyle='--', marker='s', color='red')

# Plota grafico Euler_melhorado
plt.plot(Xval_Euler_M, Yval_Euler_M, label='Método de Euler Melhorado', linestyle='-', marker='o', color='blue')

# Plota grafico Euler Ponto Medio
plt.plot(Xval_Euler_PM, Yval_Euler_PM, label='Método de Euler Ponto Medio', linestyle=':', marker='v', color='green')

plt.plot(Xval_Original, Yval_original, label='funçao original', linestyle='dotted', marker='x', color='purple')

# título e rótulo
plt.title("Métodos Numéricos")
plt.xlabel("x")
plt.ylabel("y")


# Legenda e grid
plt.grid(True)
plt.legend()

plt.show()
