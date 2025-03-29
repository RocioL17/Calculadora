import statistics

def calcular_mediana(lista):
    return statistics.median(lista)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    print("La mediana es:", calcular_mediana(numeros))
