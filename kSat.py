import random
from pysat.solvers import Solver
import matplotlib.pyplot as plt
import numpy as np

def gerar_instancia_sat(n, m, k):
    variaveis = list(range(1, n + 1))
    clausulas = []

    while len(clausulas) < m:
        vars_clausula = random.sample(variaveis, k)
        clausula = []
        for var in vars_clausula:
            if random.choice([True, False]):
                clausula.append(var)
            else:
                clausula.append(-var)
        
        # Verificae se a clausula ja existe
        if clausula not in clausulas:
            clausulas.append(clausula)
    
    return clausulas

def verificar_satisfazibilidade(clausulas):
    solver = Solver(name='glucose3')  
    for clausula in clausulas:
        solver.add_clause(clausula)
    satisfazivel = solver.solve() 
    solver.delete() 
    return satisfazivel

def calcular_probabilidade_satisfazibilidade(n, alpha, k, num_instancias=30):
    m = int(alpha * n)
    satisfaziveis = 0
    for _ in range(num_instancias):
        instancia = gerar_instancia_sat(n, m, k)
        if verificar_satisfazibilidade(instancia):
            satisfaziveis += 1
    
    probabilidade = satisfaziveis / num_instancias
   
    return probabilidade

def gerar_grafico_probabilidade(n, k, list_p, valores_alpha):
    fig, ax = plt.subplots()
    plt.title(f"Grafico de probabilidade_{k}-SAT_N={n}")
    ax.plot(valores_alpha, list_p)
    fig.savefig(f"IMAGES/PROBABILIDADE/{k}-SAT_N={n}")
    plt.show()

def gerar_grafico_tempo(n, k, valores_alpha, t):
    fig, ax = plt.subplots()
    plt.title(f"Grafico de tempo_{k}-SAT_N={n}")
    ax.plot(valores_alpha, t)
    fig.savefig(f"IMAGES/TEMPO/{k}-SAT_N={n}")
    plt.show()