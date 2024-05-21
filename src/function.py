import matplotlib.pyplot as plt
import numpy as np
import math


class Function:
    x_values: list
    y_euler: list
    y_melhorado: list
    y_ponto_medio: list
    n_passos: float
    h: int  # numero de passos para funçao

    def __init__(self, inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos: int):


        self.n_passos = n_passos
        self.x_values = [inicial[0]]
        self.y_euler = [inicial[1]]
        self.y_melhorado = [inicial[1]]
        self.y_ponto_medio = [inicial[1]]
        self.h = (intervalo[1] - intervalo[0])/n_passos

    def plot_all(self):
        """plots all graps for the numeric methods"""
        self.make_euler(True)

        self.plot_grap("metodos numericos")

    @staticmethod
    def plot_grap(title: str):
        """recives 2 list with the X and Y related values for a function, and plot it's grap"""
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

    @staticmethod
    def derivada(t, y):
        """return the numeric value for the derivate of a function in a point"""
        dy = (-y + t + 1)
        return dy
    

    @staticmethod
    def function(t):
        """return the numeric value for Y of a function in a point """
        return (t - math.e**-t)

    def euler(self, y: float, x: float):
        """function returning next value for Euler's method """
        newy = y + self.h * self.derivada(x, y)
        return newy

    def make_euler(self, plot: bool):
        """function building a list whit x an y values for Euler's mothod, it has a boolean to determine if the grap will be plotted"""
        x = self.x_values
        y = self.y_euler
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler(y[-1], x[-1])
            x.append(newx)
            y.append(newy)
            
            
        if plot is True:
            plt.plot(x, y, label='Método de Euler',
                     linestyle='--', marker='s', color='red')
        else:
            return x, y




inicial = (1, 0)
intervalo = (0, 5)
Fx = Function(inicial, intervalo, 10)
Fx.make_euler(True)
Fx.plot_grap('Euler')