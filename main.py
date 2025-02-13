import time
from kSat import calcular_probabilidade_satisfazibilidade
import pysat

def main():
    valores_n = [50, 100, 150, 200]  # Valores de n
    valores_alpha = [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0]  # Valores de alpha
    k = 3  # Tamanho das cláusulas (3-SAT)

    for n in valores_n:
        print(f"n = {n}")
        for alpha in valores_alpha:
            inicio = time.time()
            probabilidade = calcular_probabilidade_satisfazibilidade(n, alpha, k)
            fim = time.time()
            print(f"  alpha = {alpha}: Probabilidade = {probabilidade:.4f}, Tempo = {fim - inicio:.2f} segundos")
        print()

if __name__ == "__main__":
    main()