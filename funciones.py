#Módulo encargado de la lógica de procesar las calificaciones y la generación de reportes

#Trae las herramientas matemáticas y de validación desde el archivo utilidades
from utilidades import validar_nota, validar_opcion, suma_recursiva

#Función para pedir las notas de una asignatura a través del teclado
def ingresar_notas(nombre_asignatura):
    notas = []    #Crea una lista vacía para guardar las notas de esta asignatura

    #Ciclo: Pregunta cuántas notas tiene esta asignatura y evita que el usuario ingrese letras
    while True:
        try:
            cantidad = int(input(f"¿Cuántas notas tiene {nombre_asignatura}?: "))
            if cantidad > 0:
                break    #Si el número es mayor a 0 se quiebra el ciclo
            print("Debe ingresar al menos una nota.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    #Pregunta las notas una por una según la cantidad total ingresada anteriomente
    for i in range(cantidad):
        #Valida que la nota esté entre 1.0 y 7.0
        nota = validar_nota(i + 1)
        notas.append(nota)  #Agrega la nota a la lista
    #Devuelve una tupla con el nombre de la materia y todas sus notas desglosadas
    return (nombre_asignatura, *notas)

#Función para mostrar el menú de las materias y dejar que el usuario elija
def seleccionar_asignaturas():
    asignaturas = []    #Crea una lista para guardar las materias elegidas con sus notas
    asignaturas_ingresadas = set()  #Set o conjunto que ayuda a no repetir materias

    #Diccionario para asociar cada número del menú con el nombre de una asignatura
    menu_asignaturas = {
        1: "Matemática",
        2: "Historia",
        3: "Lenguaje",
        4: "Artes",
        5: "Educación Física",
        6: "Química",
        7: "Física",
        8: "Biología"
    }

    #Ciclo que muestra el menú una y otra vez hasta que el usuario decida terminar
    while True:
        print("""
===================================
        MENÚ ASIGNATURAS
===================================
1. Matemática
2. Historia
3. Lenguaje
4. Artes
5. Educación Física
6. Química
7. Física
8. Biología
9. Finalizar ingreso
===================================
""")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número entero.")
            continue    #Si el usuario pone letras, ignora el resto del código y vuelve a empezar el ciclo

        #Valida que el número esté en el rango del menú (1 al 9)
        if not validar_opcion(opcion, 1, 9):
            print("Opción fuera de rango. Intente nuevamente.")
            continue

        #Si elige la opción 9, se termina el ingreso de materias para este alumno
        if opcion == 9:
            break

        #Busca el nombre de la materia en el diccionario usando el número ingresado
        nombre = menu_asignaturas[opcion]

        #Revisa en el 'set' si esa materia ya la había ingresado antes
        if nombre in asignaturas_ingresadas:
            print(f"La asignatura '{nombre}' ya fue ingresada.")
            continue

        asignaturas_ingresadas.add(nombre)  #Si es nueva, la registra en el 'set' para que no la pueda volver a ingresar
        datos_asignatura = ingresar_notas(nombre)   #Llama la función de arriba para pedir las notas de esta materia
        asignaturas.append(datos_asignatura)    #Guarda todo en la lista

    #Convierte la lista en una tupla antes de enviarla de vuelta para que sea inmutable
    return tuple(asignaturas)

#Función para calcular el promedio de una sola asignatura
def calcular_promedio(asignatura):
    notas = list(asignatura[1:])    #Separa solo las notas (quitando el nombre de la materia que está en la posición 0)
    suma = suma_recursiva(notas)    #Suma las notas usando la función recursiva
    return suma / len(notas)        #Divide la suma total por la cantidad de notas para obtener el promedio

#Función para mostrar el reporte del alumno en la pantalla
def mostrar_alumno(alumno):
    nombre_alumno = alumno[0]   #Agrega el nombre en la primera posición
    asignaturas_alumno = alumno[1:] #Agrega luego las materias y las notas

    print(f"\nAlumno: {nombre_alumno}")
    promedios = {}
    suma_general = 0
    cantidad_asignaturas = 0

    #Procesa cada materia del alumno por separado
    for asignatura in asignaturas_alumno:
        promedio = calcular_promedio(asignatura)    #Calcula el promedio
        nombre_materia = asignatura[0]
        notas_materia = asignatura[1:]

        promedios[nombre_materia] = promedio    #Guarda el promedio en un diccionario

        print(f" * Asignatura: {nombre_materia}")
        print(f"   Notas: {', '.join(map(str, notas_materia))}")    #Muestra las notas de forma ordenada, separadas por comas
        print(f"   Promedio: {promedio:.2f}")

        suma_general += promedio    #Suma todo para calcular al final el promedio general de todas sus materias
        cantidad_asignaturas += 1

    #Saca el promedio general y evita dividir por cero si no tiene materias
    promedio_general = (suma_general / cantidad_asignaturas) if cantidad_asignaturas > 0 else 0.0

    #Imprime el resumen al final
    print("------ Resumen ------")
    for nombre, promedio in promedios.items():
        print(f" * {nombre:<20}: {promedio:.2f}")
    print(f"Promedio General: {promedio_general:.2f}\n")

#Función que procesa un archivo csv externo y genera otro ordenado
def procesar_archivo_externo(nombre_entrada, nombre_salida):
    """
    Lee un archivo CSV con formato (nombre,apellido,asignatura,nota1,nota2,nota3),
    los calcula, los clasifica, los ordena por asignatura y los guarda en un output.
    """
    try:
        #Abre el archivo de origen
        with open(nombre_entrada, mode="r", encoding="utf-8") as entrada:
            lineas = entrada.readlines()    #Guarda cada fila del archivo como un texto en una lista

        #Si el archivo no tiene filas o solo tiene los títulos, avisa el error    
        if len(lineas) <= 1:
            print("[ERROR] El archivo de entrada está vacío o solo contiene cabeceras.")
            return

        registros_procesados = []   #Crea una lista para guardar los datos calculados

       #Recorre el archivo desde la línea 1 y salta la línea 0 que son los títulos
        for linea in lineas[1:]:
            #Con strip() borra los saltos de línea invisibles y split(",") separa los datos por comas
            datos = linea.strip().split(",")
            if len(datos) < 6:
                continue    #Si a la fila le faltan datos, se la salta para no romper el programa
            
            #Guarda las primeras 3 columnas en variables
            nombre, apellido, asignatura = datos[0], datos[1], datos[2]
            
            try:
                #Convierte las notas de texto a números decimales
                notas = [float(datos[3]), float(datos[4]), float(datos[5])]
            except ValueError:
                continue #Si alguna nota tiene letras en el archivo, se salta esa fila entera
            
            #Hace los cálculos matemáticos automáticos
            suma_notas = suma_recursiva(notas)
            promedio = round(suma_notas / len(notas), 2)
            #Evalúa si aprueba o reprueba según la escala tradicional
            estado = "APROBADO" if promedio >= 4.0 else "REPROBADO"
            
           #Guarda la información en un diccionario temporal
            registros_procesados.append({
                "nombre": nombre,
                "apellido": apellido,
                "asignatura": asignatura,
                "nota1": notas[0],
                "nota2": notas[1],
                "nota3": notas[2],
                "promedio": promedio,
                "estado": estado
            })

        #Ordena toda la lista alfabéticamente por la columna 'asignatura'
        registros_procesados.sort(key=lambda x: x["asignatura"])

        #Creamos el archivo de salida para escribir los resultados finales
        with open(nombre_salida, mode="w", encoding="utf-8") as salida:
            salida.write("nombre,apellido,asignatura,nota1,nota2,nota3,promedio,estado\n")
            for r in registros_procesados:
                #Escribe los títulos de las nuevas columnas en la primera fila
                salida.write(f"{r['nombre']},{r['apellido']},{r['asignatura']},{r['nota1']},{r['nota2']},{r['nota3']},{r['promedio']:.2f},{r['estado']}\n")
                
        print(f"\n[ÉXITO] Archivo procesado y ordenado por asignatura. Guardado en '{nombre_salida}'.")

    except FileNotFoundError:   #Si el archivo no existe o no se puede abrir, el programa no se cae
        print(f"[ERROR] El archivo '{nombre_entrada}' no existe en la carpeta del proyecto.")
    except IOError:
        print("[ERROR] No se pudo leer o escribir la información del archivo.")