import matplotlib.pyplot as plt
import numpy as np
import math

class Function:
    
    inicial: 'tuple[float, float]'
    intervalo: 'tuple[float, float]'
    x_values: list
    y_euler: list
    y_melhorado: list
    y_ponto_medio: list
    
    h: int # numero de passos para funçao
    def __init__(self, intervalo: 'tuple[float, float]',inicial: 'tuple[float, float]', n_passos: int):
        self.intervalo = intervalo
        self.h = n_passos
        self.x_values = [inicial[0]]
        self.y_euler = inicial[1]
        self.y_melhorado = inicial[1]
        self.y_ponto_medio = inicial[1]
        
    @staticmethod
    def derivada(t, y):
        return(-y + t + 1)
    @staticmethod
    def function(t, y):
        return (t - math.e**-t)
    @staticmethod
    def Euler():
        return
        
