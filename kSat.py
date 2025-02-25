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
    fig.savefig(f"IMAGES/PROBABILIDADE/PROBABILIDADE_{k}-SAT_N={n}")
    plt.show()

def gerar_grafico_tempo(n, k, valores_alpha, t):
    fig, ax = plt.subplots()
    plt.title(f"Grafico de tempo_{k}-SAT_N={n}")
    ax.plot(valores_alpha, t)
    fig.savefig(f"IMAGES/TEMPO/TEMPO_{k}-SAT_N={n}")
    plt.show()


def gerar_graficos_totais_p(k, valores_alpha, lista_total):
    fig, ax = plt.subplots()
    plt.title(f"Grafico de probabilidade de satisfazibilidade para {k}-SAT")
    
    if k==5:
        n_values = [10,20,30,40,50,60]
    elif k==3:
        n_values = [50, 100, 150, 200]
    # Adiciona cada lista de probabilidades ao gráfico
    for i, list_p in enumerate(lista_total):
        ax.plot(valores_alpha, list_p, label=f'N={n_values[i]}')
    
    ax.set_xlabel('Alpha (m/n)')
    ax.set_ylabel('Probabilidade de Satisfazibilidade')
    ax.legend()
    ax.grid(True)
    
    fig.savefig(f"IMAGES/PROBABILIDADE/PROBABILIDADE_TOTAL_{k}-SAT.png")
    plt.show()


def gerar_graficos_totais_t(k, valores_alpha, lista_total):
    fig, ax = plt.subplots()
    plt.title(f"Grafico de tempo {k}-SAT")
    
    if k==5:
        n_values = [10,20,30,40,50,60]
    elif k==3:
        n_values = [50, 100, 150, 200]
    # Adiciona cada lista de probabilidades ao gráfico
        for i, list_t in enumerate(lista_total):
            ax.plot(valores_alpha, list_t, label=f'N={n_values[i]}')
    
    ax.set_xlabel('Alpha (m/n)')
    ax.set_ylabel('Tempo')
    ax.legend()
    ax.grid(True)
    
    fig.savefig(f"IMAGES/TEMPO/TEMPO_TOTAL_{k}-SAT.png")
    plt.show()


