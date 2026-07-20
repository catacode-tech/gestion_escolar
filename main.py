#Archivo principal: controla el menú y decide que flujo usará el programa

#Traemos las funciones creadas en el archivo funciones para usarlas aquí
from funciones import seleccionar_asignaturas, mostrar_alumno, procesar_archivo_externo

def iniciar_sistema():
    #Mostramos el archivo de bienvenida en la pantalla
    print("""
==================================================
    SISTEMA DE GESTIÓN ESCOLAR Y REGISTRO 
              DE CALIFICACIONES
==================================================
""")
    #Le mostramos las dos opciones disponibles al usuario: manual o automática
    print("Seleccione el método de entrada de datos:")
    print("1) Registrar datos manualmente por consola")
    print("2) Cargar archivo externo ('import.csv') automáticamente")
    print("==================================================")
    
    #Ciclo 1: Asegura que el usuario elija solo una opción válida (1 o 2)
    while True:
        opcion = input("Ingrese una opción (1 o 2): ").strip() #Borra los espacios para evitar errores
        if opcion in ("1", "2"):
            break   #Si escribió 1 o 2 se rompe el ciclo porque el dato es correcto
        print("Opción no válida. Digite 1 o 2.") #Si escribió otra cosa, el sistema le avisa y le vuelve a preguntar 1 o 2 

    if opcion == "1":  #Si el usuario ingresa las notas de manera manual a través del teclado
        alumnos = []  #Crea una lista vacía para ir guardando a los estudiantes

        #Ciclo 2: pregunta cuántos alumnos va a registrar
        while True:
            try:
                cantidad_alumnos = int(input("\nIngrese la cantidad de alumnos a registrar: "))
                if cantidad_alumnos > 0:  #La cantidad de alumnos debe ser mayor a 0
                    break   
                print("Debe ingresar un número mayor que cero.")
            except ValueError:     #Asegura que el usuario ingrese números y no letras
                print("Debe ingresar un número entero válido.") 

        #Ciclo 3: Se repite según la cantidad de alumnos que el usuario indicó antes
        for i in range(cantidad_alumnos):
            print(f"\n--- Registro del alumno {i + 1} ---")
            
            #Ciclo 4: Asegura que el usuario no deje el nombre en blanco
            while True:
                nombre = input("Nombre del alumno: ").strip()
                if nombre:
                    break
                print("El nombre no puede estar vacío. Inténtelo de nuevo.")

            #Llama a la función que abre el menú para elegir materias y poner notas
            asignaturas = seleccionar_asignaturas()
            #Une el nombre del alumno y sus materias en una sola estructura (Tupla)
            alumno = (nombre,) + asignaturas
            #Guarda todos los datos del alumno dentro de la lista principal
            alumnos.append(alumno)

        #Imprime en pantalla el reporte de lo que se ingresó a mano
        print("\n==============================================")
        print("                REPORTE FINAL")
        print("==============================================")
        #Llama a la función que calcula promedios y los muestra
        for alumno in alumnos:
            mostrar_alumno(alumno)

    #Si el usuario eligió la opción 2 ingresa las notas de manera automática a través de un archivo csv         
    elif opcion == "2":
        print("\n[PROCESANDO] Leyendo 'import.csv'...")
        procesar_archivo_externo("import.csv", "output.csv")  #Lee el archivo de entrada, calcula los promedios y crea el archivo output que indica si el estudisnte aprobó o reprobó la asignatura

    #Mensaje final para cerrar el programa
    print("""
==================================================
¡Proceso finalizado con éxito! 
Gracias por utilizar nuestro sistema escolar.
==================================================
""")
# Esto permite que al ejecutar este archivo arranque el sistema
if __name__ == "__main__":
    iniciar_sistema()