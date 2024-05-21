import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os


class Function:
    def __init__(self, inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos: int):
        self.inicial = inicial
        self.n_passos = n_passos
        self.y_origial = [inicial[1]]
        self.y_euler = [inicial[1]]
        self.y_melhorado = [inicial[1]]
        self.y_ponto_medio = [inicial[1]]
        self.h = (intervalo[1] - intervalo[0])/n_passos

    def export_to_excel(self, arquivo: str):
        """Exports the computed values to an Excel file"""

        x_original, y_original = self.make_original(False)
        x_euler, y_euler = self.make_euler(False)
        x_melhorado, y_melhorado = self.make_euler_melhorado(False)
        x_ponto_medio, y_ponto_medio = self.make_euler_ponto_medio(False)

        data = {
            "X": x_original,
            "Original": y_original,
            "Euler": y_euler,
            "Euler Melhorado": y_melhorado,
            "Euler Ponto Médio": y_ponto_medio
        }

        df = pd.DataFrame(data)
        df.to_excel(arquivo, index=False, engine='openpyxl')
        print(f"Data exported to {arquivo}")

    def plot_all(self):
        """plots all graphs for the numeric methods"""
        self.make_original(True)
        self.make_euler(True)
        self.make_euler_melhorado(True)
        self.make_euler_ponto_medio(True)
        self.plot_graph("Métodos Numéricos")

    def plot_graph(self, title: str):
        """receives 2 lists with the X and Y related values for a function, and plots its graph"""
        plt.title(title)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

    @staticmethod
    def derivada(t, y):
        """returns the numeric value for the derivative of a function at a point"""
        dy = (-y + t + 1)
        return dy

    @staticmethod
    def function(t):
        """returns the numeric value for Y of a function at a point"""
        dy = t + (math.e**-t)
        return dy

    def euler(self, y: float, x: float):
        """returns the next value for Euler's m
        ethod"""
        newy = y + self.h * self.derivada(x, y)
        return newy

    def euler_melhorado(self, x: float, y: float):
        """returns the next iteration for improved Euler's method"""
        k1 = self.derivada(x, y)
        x2 = x + self.h
        y2 = y + self.h * k1
        k2 = self.derivada(x2, y2)
        dy = y + ((self.h/2) * (k1 + k2))
        return dy

    def euler_ponto_medio(self, x: float, y: float):
        """returns the next iteration for Euler's midpoint method"""
        k1 = self.derivada(x, y)
        x2 = x + (self.h/2)
        y2 = y + (self.h/2) * k1
        k2 = self.derivada(x2, y2)
        dy = y + self.h * k2
        return dy

    def make_original(self, plot: bool):
        """plots the original function"""
        x = [self.inicial[0]]
        y = self.y_origial
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.function(x[-1])
            x.append(newx)
            y.append(newy)
        if plot:
            plt.plot(x, y, label='F(x, y)', linestyle='solid',
                     marker='x', color='purple')
        else:
            return x, y

    def make_euler(self, plot: bool):
        """builds a list with x and y values for Euler's method; it has a boolean to determine if the graph will be plotted or not"""
        x = [self.inicial[0]]
        y = self.y_euler
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler(y[-1], x[-1])
            x.append(newx)
            y.append(newy)
        if plot:
            plt.plot(x, y, label='Método de Euler',
                     linestyle='--', marker='s', color='red')
        else:
            return x, y

    def make_euler_melhorado(self, plot: bool):
        """builds a list with x and y values for improved Euler's method; it has a boolean to determine if the graph will be plotted or not"""
        x = [self.inicial[0]]
        y = self.y_melhorado
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler_melhorado(x[-1], y[-1])
            x.append(newx)
            y.append(newy)
        if plot:
            plt.plot(x, y, label='Método de Euler Melhorado',
                     linestyle='-', marker='o', color='blue')
        else:
            return x, y

    def make_euler_ponto_medio(self, plot: bool):
        """builds a list with x and y values for Euler's midpoint method; it has a boolean to determine if the graph will be plotted or not"""
        x = [self.inicial[0]]
        y = self.y_ponto_medio
        h = self.h
        for _ in range(self.n_passos):
            newx = x[-1] + h
            newy = self.euler_ponto_medio(x[-1], y[-1])
            x.append(newx)
            y.append(newy)
        if plot:
            plt.plot(x, y, label='Método de Euler Ponto Médio',
                     linestyle=':', marker='v', color='green')
        else:
            return x, y

