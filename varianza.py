import statistics

def calcular_varianza(lista):
    if len(lista) < 2:
        return "Se necesitan al menos dos números para calcular la varianza."
    return statistics.variance(lista)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    print("La varianza es:", calcular_varianza(numeros))
