import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import os
from function import Function as Fx


def monta_database(database: pd.DataFrame, a, y_values: list):
    """adiciona uma nova coluna em uma planilha"""
    aux: str
    aux = a
    database[aux] = y_values


def export_to_excel(database: pd.DataFrame, arquivo: str):
    """Exports the computed values to an Excel file"""

    database.to_excel(arquivo, index=False, engine='openpyxl')
    print(f"Data exported to {arquivo}")


def achavalores(F: Fx, x: float, y: float, a, b, p, q):
    """funcao qe faz coisas"""
    h = F.h
    K1 = F.derivada(x, y)
    K2 = F.derivada(x + p * h, y + q * h * F.derivada(x, y))
    dy = (a*K1 + b*K2)
    return dy


def faz_coisas(a: float, F: Fx, df: pd.DataFrame):
    """"teste"""
    b = 1 - a
    q = 0.5/b
    print(q)
    p = q
    x = [F.inicial[0]]
    y = [F.inicial[1]]
    for _ in range(F.n_passos):
        newx = x[-1] + F.h
        newy = achavalores(F, x[-1], y[-1], a, b, p, q)

        x.append(newx)
        y.append(newy)
    monta_database(df, a, y)


def make_achavalores(F: Fx):
    """d dddd sdsad asdad adaaadd swd dd"""
    data = {}
    df = pd.DataFrame(data)
    a = 0
    while a < 0.9:
        faz_coisas(a, F, df)
        a = a + 0.3
    export_to_excel(df, "melhor valor.xlsx")
