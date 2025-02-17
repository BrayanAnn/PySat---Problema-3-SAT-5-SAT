import time
from kSat import calcular_probabilidade_satisfazibilidade, gerar_grafico_probabilidade, gerar_grafico_tempo
import numpy as np

def testar_sat(valores_n, valores_alpha, k, nome_sat):
    
    print(f"Testando {nome_sat} (k = {k})")
    for n in valores_n:
        list_probabilidade = []
        list_tempo = []
        print(f"n = {n}")
        for alpha in valores_alpha:
            inicio = time.time()
            probabilidade = calcular_probabilidade_satisfazibilidade(n, alpha, k)
            fim = time.time()
            tempo = round(float(fim - inicio), 2)
            print(f"  alpha = {alpha}: Probabilidade = {probabilidade:.4f}, Tempo = {tempo} segundos")
            list_probabilidade.append(probabilidade)
            list_tempo.append(tempo)
        if list_probabilidade != None:
            gerar_grafico_probabilidade(n, k, list_probabilidade, valores_alpha)
            gerar_grafico_tempo(n, k, valores_alpha, list_tempo)
        print()

def main():
    valores_n = [50, 100, 150, 200]  # Valores de n
    valores_alpha_3sat = [round(valor, 1) for valor in np.arange(3.0, 5.1, 0.1)] # de 3 a 5 incremendantpo 0.1
    valores_alpha_5sat = [round(valor, 1) for valor in np.arange(1, 20.1, 0.1)]# de 1 a 20 incremendanto 0.1

    # Testar 3-SAT
    testar_sat(valores_n, valores_alpha_3sat, k=3, nome_sat="3-SAT")
    

    # Testar 5-SAT
    testar_sat(valores_n, valores_alpha_5sat, k=5, nome_sat="5-SAT")

if __name__ == "__main__":
    main()