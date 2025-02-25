import time
from kSat import calcular_probabilidade_satisfazibilidade, gerar_grafico_probabilidade, gerar_grafico_tempo, gerar_graficos_totais_p, gerar_graficos_totais_t
import numpy as np

def testar_sat(valores_n, valores_alpha, k, nome_sat):
    list_probabilidade_totais_n = []
    list_tempo_totais_n = []
    print(f"Testando {nome_sat} (k = {k})")
    for n in valores_n:
        list_probabilidade = []
        list_tempo = []
        print(f"n = {n}")
        for alpha in valores_alpha:
            inicio = time.time()
            probabilidade = calcular_probabilidade_satisfazibilidade(n, alpha, k)
            fim = time.time()
            tempo = round(float(fim - inicio), 4)
            print(f"  alpha = {alpha}: Probabilidade = {probabilidade:.6f}, Tempo = {tempo} segundos")
            list_probabilidade.append(probabilidade)
            list_tempo.append(tempo)
        if list_probabilidade != None:
            gerar_grafico_probabilidade(n, k, list_probabilidade, valores_alpha)
            gerar_grafico_tempo(n, k, valores_alpha, list_tempo)
        list_probabilidade_totais_n.append(list_probabilidade)
        list_tempo_totais_n.append(list_tempo)
    gerar_graficos_totais_p(k, valores_alpha, list_probabilidade_totais_n)
    gerar_graficos_totais_t(k, valores_alpha, list_tempo_totais_n)
    print()


def main():
    valores_n_3sat = [50, 100, 150, 200]  # Valores de n
    valores_n_5sat = [10, 20, 30, 40, 50]
    valores_alpha_3sat = [round(valor, 1) for valor in np.arange(1, 10.1, 0.1)] # de 3 a 5 incremendantpo 0.1
    valores_alpha_5sat = [round(valor, 1) for valor in np.arange(1, 30.1, 0.1)]# de 1 a 20 incremendanto 0.1

    # Testar 3-SAT
    testar_sat(valores_n_3sat, valores_alpha_3sat, k=3, nome_sat="3-SAT")
    

    # Testar 5-SAT
    testar_sat(valores_n_5sat, valores_alpha_5sat, k=5, nome_sat="5-SAT")
    
if __name__ == "__main__":
    main()