import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from function import Function as Fx


def monta_database(database: pd.DataFrame, a: float, y_values: list):
    """Adiciona uma nova coluna ao DataFrame com valores de y para dado a."""
    aux = f'a={a}'
    database[aux] = y_values


def export_to_excel(database: pd.DataFrame, arquivo: str):
    """Exporta o DataFrame para um arquivo Excel."""
    try:
        database.to_excel(arquivo, index=False, engine='openpyxl')
        print(f"Dados exportados para {arquivo}")
    except Exception as e:
        print(f"Erro ao exportar dados para {arquivo}: {e}")


def achavalores(F: Fx, x: float, y: float, a: float, b: float, p: float, q: float) -> float:
    """Calcula o próximo valor de y usando o método numérico."""
    h = F.h
    K1 = F.derivada(x, y)
    K2 = F.derivada(x + p * h, y + q * h * K1)
    dy = a * K1 + b * K2

    # Debugging prints
    print(f"x: {x}, y: {y}, a: {a}, b: {b}, K1: {K1}, K2: {K2}, dy: {dy}")

    return y + dy * h


def faz_coisas(a: float, F: Fx, df: pd.DataFrame):
    """Executa cálculos para diferentes valores de 'a' e atualiza o DataFrame."""
    b = 1 - a
    if b == 0:
        return  # Pula a iteração se b for zero
    q = 0.5 / b
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
    """Gera valores para diferentes parâmetros 'a' e exporta para Excel."""
    data = {}
    df = pd.DataFrame(data)
    a_values = np.arange(0.0, 1.0, 0.1)
    for a in a_values:
        faz_coisas(a, F, df)
    export_to_excel(df, "melhor_valor.xlsx")

    # Plotando os resultados
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    plt.xlabel('Passos')
    plt.ylabel('Valores de y')
    plt.title('Comparação de y para diferentes valores de a')
    plt.legend()
    plt.show()
