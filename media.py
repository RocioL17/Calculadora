import statistics

def calcular_media(lista):
    return statistics.mean(lista)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    print("La media es:", calcular_media(numeros))
