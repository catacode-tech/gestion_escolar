# Documentación técnica del Sistema de Gestión Escolar y Registro de Calificaciones
1. **Descripción del Sistema**
El "Sistema de Gestión Escolar y Registro de Calificaciones" es una aplicación de consola desarrollada en Python. Su diseño contempla programación modular para registrar estudiantes, asociar asignaturas personalizadas, registrar calificaciones con validaciones de rango (entre 1.0 y 7.0), calcular promedios mediante recursividad y emitir informes de rendimiento escolar individuales y generales.
2. **Estructuras de Datos Utilizadas**
    * Listas (list): Utilizadas para almacenar colecciones dinámicas de datos que cambian durante la ejecución, como la lista global de alumnos y las calificaciones individuales ingresadas temporalmente en notas.
    * Diccionarios (dict): Utilizados en dos áreas clave:
        1. Mapeo dinámico y escalable del menú de asignaturas (pares ID: "Nombre Asignatura").
        2. Asociación clave-valor de promedios finales por materia en la ficha del alumno (pares "Asignatura": promedio).
    * Tuplas (tuple): Utilizadas para empaquetar y resguardar la inmutabilidad de los datos finales del estudiante y sus asignaturas:
      alumno = (Nombre, (Asignatura1, nota1, nota2), (Asignatura2, nota1))
    * Conjuntos (set): Utilizados para llevar registro de las asignaturas seleccionadas (asignaturas_ingresadas) y garantizar que no se registren materias duplicadas en un mismo estudiante de forma eficiente ($O(1)$).
3. **Funcionalidades Implementadas**
    * Módulo de Validación: Control de entrada de datos numéricos y manejo de excepciones (try-except) ante ingresos de texto o vacíos.
    * Cálculo Recursivo: Implementación de algoritmo recursivo para la suma de listas de calificaciones, reduciendo el acoplamiento con funciones nativas.
    * Reportabilidad: Interfaz formateada en consola que detalla el rendimiento asignatura por asignatura y calcula el promedio general del alumno de manera segura (previniendo divisiones por cero).


