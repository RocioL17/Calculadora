from scipy.stats import trim_mean

def calcular_media_recortada(lista, porcentaje):
    return trim_mean(lista, porcentaje)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    porcentaje = float(input("Ingresa el porcentaje a recortar (ejemplo: 0.1 para 10%): "))
    print("La media recortada es:", calcular_media_recortada(numeros, porcentaje))
