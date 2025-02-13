import random
from pysat.solvers import Solver

def gerar_instancia_sat(n, m, k):
    variaveis = list(range(1, n + 1))
    clausulas = []

    while len(clausulas) < m:
        # Seleciona k variáveis distintas
        vars_clausula = random.sample(variaveis, k)
        
        # Decide aleatoriamente se cada variável será positiva ou negada
        clausula = []
        for var in vars_clausula:
            if random.choice([True, False]):
                clausula.append(var)
            else:
                clausula.append(-var)
        
        # Verifica se a cláusula já existe
        if clausula not in clausulas:
            clausulas.append(clausula)
    
    return clausulas

def verificar_satisfazibilidade(clausulas):
    solver = Solver(name='glucose3')  # Usando o solver Glucose
    for clausula in clausulas:
        solver.add_clause(clausula)  # Adiciona cada cláusula ao solver
    satisfazivel = solver.solve()  # Verifica se é satisfazível
    solver.delete()  # Libera a memória do solver
    return satisfazivel

def calcular_probabilidade_satisfazibilidade(n, alpha, k, num_instancias=30):
    m = int(alpha * n)  # Número de cláusulas
    satisfaziveis = 0

    for _ in range(num_instancias):
        instancia = gerar_instancia_sat(n, m, k)
        if verificar_satisfazibilidade(instancia):
            satisfaziveis += 1
    
    probabilidade = satisfaziveis / num_instancias
    return probabilidade