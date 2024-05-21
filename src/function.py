import matplotlib.pyplot as plt
import numpy as np
import math


class Function:
    inicial: 'tuple[float, float]'
    y_origial: list
    y_euler: list
    y_melhorado: list
    y_ponto_medio: list
    n_passos: float
    h: int  # numero de passos para funçao

    def __init__(self, inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos: int):
        self.inicial = inicial
        self.n_passos = n_passos
        self.y_origial = [inicial[1]]
        self.y_euler = [inicial[1]]
        self.y_melhorado = [inicial[1]]
        self.y_ponto_medio = [inicial[1]]
        self.h = (intervalo[1] - intervalo[0])/n_passos

    def plot_all(self):
        """plots all graps for the numeric methods"""
        self.make_original(True)
        self.make_euler(True)
        self.make_euler_melhorado(True)
        self.make_euler_ponto_medio(True)
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
        dy = t - (math.e**-t)
        return dy

    def euler(self, y: float, x: float):
        """function returning next value for Euler's method """
        newy = y + self.h * self.derivada(x, y)
        return newy

    def euler_melhorado(self, x: float, y: float):
        """returns the next iteration for improved euler's method"""
        k1 = self.derivada(x, y)
        x2 = x + self.h
        y2 = y + self.h * k1
        k2 = self.derivada(x2, y2)
        dy = y + ((self.h/2) * (k1 + k2))
        return dy

    def euler_ponto_medio(self, x: float, y: float):
        """returns the next iteration for  euler's middle point method"""
        k1 = self.derivada(x, y)
        x2 = x + (self.h/2)
        y2 = y + (self.h/2) * k1
        k2 = self.derivada(x2, y2)
        dy = y + self.h * k2
        return dy

    def make_original(self, plot: bool):
        """plota a funçao original """
        x = [inicial[0]]
        y = self.y_origial
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.function(x[-1])
            x.append(newx)
            y.append(newy)
        if plot is True:
            plt.plot(x, y, label='F(x, y)',
                     linestyle='solid', marker='x', color='purple')
        else:
            return x, y

    def make_euler(self, plot: bool):
        """function building a list whit x an y values for Euler's mothod, it has a boolean to determine if the grap will be plotted or not"""
        x = [inicial[0]]
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

    def make_euler_melhorado(self, plot: bool):
        """function building a list whit x an y values for improved Euler's mothod, it has a boolean to determine if the grap will be plotted or not"""
        x = [inicial[0]]
        y = self.y_melhorado
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler_melhorado(y[-1], x[-1])
            x.append(newx)
            y.append(newy)
        if plot is True:
            plt.plot(x, y, label='Método de Euler Melhorado',
                     linestyle='-', marker='o', color='blue')
        else:
            return x, y

    def make_euler_ponto_medio(self, plot: bool):
        """function building a list whit x an y values for improved Euler's mothod, it has a boolean to determine if the grap will be plotted or not"""
        x = [inicial[0]]
        y = self.y_ponto_medio
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler_ponto_medio(y[-1], x[-1])
            x.append(newx)
            y.append(newy)
        if plot is True:
            plt.plot(x, y, label='Método de Euler Ponto Medio',
                     linestyle=':', marker='v', color='green')
        else:
            return x, y


inicial = (1, 0)
intervalo = (0, 5)
Fx = Function(inicial, intervalo, 10)
Fx.plot_all()
