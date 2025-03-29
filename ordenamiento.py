def ordenar_numeros(lista):
    lista.sort()
    print("Lista ordenada:", lista)
    return lista  # Devuelve la lista ordenada para que el menú la actualice

if __name__ == "__main__":
    numeros = list(map(float, input("Ingresa una lista de números separados por espacios: ").split()))
    print("Lista ordenada:", ordenar_numeros(numeros))
