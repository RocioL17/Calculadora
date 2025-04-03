import ordenamiento
import media
import mediana
import media_recortada
import varianza
import desviacion
import matplotlib.pyplot as plt
import seaborn as sns

def mostrar_menu():
    print("\nMenú de Cálculo Estadístico")
    print("1. Ordenar números (modifica la lista)")
    print("2. Calcular media")
    print("3. Calcular mediana")
    print("4. Calcular media recortada")
    print("5. Calcular varianza")
    print("6. Calcular desviación estándar")
    print("7. Mostrar la lista actual")
    print("8. Cambiar la lista de números")
    print("9. Diagramas")
    print("10. Salir")

def mostrar_histograma(lista):
    sns.histplot(lista, bins=10, color='#722F37', kde=True)
    plt.title("Histograma")
    plt.show()

def mostrar_boxplot(lista):
    sns.boxplot(x=lista, color='#034F84')
    plt.title("Caja y Bigote")
    plt.show()

def mostrar_scatterplot(lista):
    print("\nOpciones para scatterplot:")
    print("1. Usar la misma lista")
    print("2. Ingresar una nueva lista para comparar")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        plt.scatter(range(len(lista)), lista, color='#722F37', label="Lista Original")
        plt.plot(range(len(lista)), lista, color='#034F84', linestyle='dashed')
    elif opcion == "2":
        nueva_lista = list(map(float, input("Ingresa una nueva lista de números separados por espacios: ").split()))
        plt.scatter(range(len(lista)), lista, color='#722F37', label="Lista 1")
        plt.scatter(range(len(nueva_lista)), nueva_lista, color='#034F84', label="Lista 2")
    else:
        print("Opción no válida.")
        return
    
    plt.title("Scatterplot")
    plt.legend()
    plt.show()

def mostrar_diagramas(lista):
    print("\nElige un diagrama:")
    print("1. Histograma")
    print("2. Caja y Bigote")
    print("3. Diagrama de Dispersión")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        mostrar_histograma(lista)
    elif opcion == "2":
        mostrar_boxplot(lista)
    elif opcion == "3":
        mostrar_scatterplot(lista)
    else:
        print("Opción no válida.")

def main():
    global lista_numeros
    
    def ingresar_lista():
        numeros = input("Ingresa una lista de números separados por espacios: ")
        return list(map(float, numeros.split()))
    
    lista_numeros = ingresar_lista()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            lista_numeros = ordenamiento.ordenar_numeros(lista_numeros)
            print("Lista ordenada:", lista_numeros)
        elif opcion == "2":
            print("La media es:", media.calcular_media(lista_numeros))
        elif opcion == "3":
            print("La mediana es:", mediana.calcular_mediana(lista_numeros))
        elif opcion == "4":
            porcentaje = float(input("Ingresa el porcentaje a recortar (ejemplo: 0.1 para 10%): "))
            print("La media recortada es:", media_recortada.calcular_media_recortada(lista_numeros, porcentaje))
        elif opcion == "5":
            print("La varianza es:", varianza.calcular_varianza(lista_numeros))
        elif opcion == "6":
            print("La desviación estándar es:", desviacion.calcular_desviacion_estandar(lista_numeros))
        elif opcion == "7":
            print("Lista actual:", lista_numeros)
        elif opcion == "8":
            lista_numeros = ingresar_lista()
        elif opcion == "9":
            mostrar_diagramas(lista_numeros)
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
