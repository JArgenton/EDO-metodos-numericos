from make import make_met as mk
from function import Function as Fx

class Euler_Method:
    def __init__(self, funcao: Fx):
        self.intervalo = funcao.inicial
        self.funcao = funcao
        self.name = 'Euler'
        self.make = mk(self, self.name, funcao.inicial, funcao.h, funcao.n_passos)
        
    def method(self, y: float, x: float):
        """returns the next value for Euler's method"""
        
        newy = y + self.funcao.h * self.funcao.derivada(x, y)
        return newy
