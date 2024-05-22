import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os

from Euler import Euler_Method
from Euler_Melhorado import Improved_Method


class Function:
    def __init__(self, inicial: 'tuple[float, float]', intervalo: 'tuple[float, float]', n_passos: int):
        self.intervalo = intervalo
        self.inicial = inicial
        self.n_passos = n_passos
        self.h = (intervalo[1] - intervalo[0])/n_passos
        self.Euler = Euler_Method(self)
        self.Euler_Improved = Improved_Method(self)

    def export_to_excel(self, arquivo: str):
        """Exports the computed values to an Excel file"""

        x_original, y_original = self.Euler.make.values()
        x_euler, y_euler = self.Euler_Improved.make.values()
        x_melhorado, y_melhorado = self.make_euler_melhorado(False)
        x_ponto_medio, y_ponto_medio = self.make_euler_ponto_medio(False)
        
        x_euler.clear()
        x_melhorado.clear()
        x_ponto_medio.clear()
        x_original.clear()
        
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
        self.Euler.make.plot()
        self.Euler_Improved.make.plot()
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