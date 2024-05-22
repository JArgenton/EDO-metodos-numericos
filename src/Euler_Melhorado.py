from make import make_met as mk
from function import Function as Fx

class Improved_Method:
    def __init__(self, funcao: Fx):
        self.intervalo = funcao.inicial
        self.funcao = funcao
        self.name = 'Euler Improved'
        self.make = mk(self, self.name, funcao.inicial, funcao.h, funcao.n_passos)
        
    def method(self, x: float, y: float):
        """returns the next iteration for improved Euler's method"""
        k1 = self.funcao.derivada(x, y)
        x2 = x + self.funcao.h
        y2 = y + self.funcao.h * k1
        k2 = self.funcao.derivada(x2, y2)
        dy = y + ((self.funcao.h/2) * (k1 + k2))
        return dy