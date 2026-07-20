# Módulo de utilidades para validaciones de datos y operaciones matemáticas

#Función para pedir una nota y asegurarse de que sea correcta (entre 1.0 y 7.0)
def validar_nota(numero):
    #Ciclo para asegurar que se ingrese una nota válida
    while True:
        try:
            #Solicita la nota al usuario convirtiéndola a decimal
            nota = float(input(f"Ingrese la nota {numero}: "))

            #Valida el rango de la nota según la escala del 1.0 al 7.0
            if nota < 1.0:
                print("La nota mínima es 1.0")
            elif nota > 7.0:
                print("La nota máxima es 7.0")
            else:
                #Retorna la nota válida y rompe el ciclo
                return nota
                
        except ValueError:
            #Advierte el error si el usuario ingresa letras o símbolos
            print("Error: Debe ingresar un valor numérico decimal (Ej: 5.5).")  #Advierte probables errores de escritura de la nota

#Función que revisa si un número del menú está dentro del rango correcto
def validar_opcion(opcion, minimo, maximo):
    # Retorna True (verdadero) si la opción está en el rango permitido, de lo contrario False (falso)
    return minimo <= opcion <= maximo

#Función que suma una lista de números usando recursividad
def suma_recursiva(lista, indice=0):
    #Cuando llega al final de la lista detiene la función y devuelve 0.0
    if indice == len(lista):
        return 0.0

    # Suma el elemento actual con el resultado de la llamada recursiva para el siguiente índice
    return lista[indice] + suma_recursiva(lista, indice + 1)