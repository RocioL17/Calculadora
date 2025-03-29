import ordenamiento
import media
import mediana
import media_recortada
import varianza
import desviacion

def mostrar_menu():
    print("\nMenú de Cálculo Estadístico")
    print("1. Ordenar números (modifica la lista)")
    print("2. Calcular media")
    print("3. Calcular mediana")
    print("4. Calcular media recortada")
    print("5. Calcular varianza")
    print("6. Calcular desviación estándar")
    print("7. Mostrar la lista actual")
    print("8. Salir")

def main():
    global lista_numeros
    numeros = input("Ingresa una lista de números separados por espacios: ")
    lista_numeros = list(map(float, numeros.split()))

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            lista_numeros = ordenamiento.ordenar_numeros(lista_numeros)
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
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
