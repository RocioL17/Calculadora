from scipy import stats

def calcular_percentil(data, p):
    return stats.scoreatpercentile(data, p)

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    porcentaje = float(input("Ingresa el número de percentil (ejemplo: 50 para 50%): "))
    print(f"El percentil {porcentaje}% es:", calcular_percentil(numeros, porcentaje))