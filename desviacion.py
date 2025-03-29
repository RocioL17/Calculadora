import statistics

def calcular_desviacion_estandar(lista):
    if len(lista) < 2:
        return "Se necesitan al menos dos números para calcular la desviación estándar."
    return statistics.stdev(lista)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    print("La desviación estándar es:", calcular_desviacion_estandar(numeros))
