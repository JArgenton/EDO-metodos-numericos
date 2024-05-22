import matplotlib.pyplot as plt
import numpy as np

class make_met:
    def __init__(self, method, name:str, inicial, h, passos):
        self.method = method
        self.name = name
        self.inicial = inicial
        self.h = h
        self.passos = passos
    def values(self):
        """builds a list with x and y values for Euler's method; it has a boolean to determine if the graph will be plotted or not"""
        x = [self.inicial[0]]  
        y = [self.inicial[1]]
        h = self.h
        for _ in range(self.passos):
            newx = x[-1] + h
            newy = self.method.method(y[-1], x[-1])
            print(newy)
            x.append(newx)
            y.append(newy)
        
        return x, y
        
    def plot(self):
        x, y = self.values()
        plt.plot(x, y, label='F(x, y)', linestyle='solid',marker='x', color='purple')
        
    def graph(self):
        self.plot()        
        plt.title(self.name)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()