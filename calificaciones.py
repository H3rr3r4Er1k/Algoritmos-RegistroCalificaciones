import csv
from alumno import Alumno

def cargar_calificaciones(archivo):
    lista_alumnos = []

    with open(archivo, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Saltar la línea de encabezado

        for row in reader:
            alumno = Alumno(row[0], row[1], row[2], row[3], row[4], row[5])
            lista_alumnos.append(alumno)

    return lista_alumnos

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high].apellidos
    i = low - 1

    for j in range(low, high):
        if arr[j].apellidos <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def calcular_nota_final(lista_alumnos):
    for alumno in lista_alumnos:
        nota_parciales = (alumno.parcial1 + alumno.parcial2) / 2 * 0.3
        nota_practico = alumno.practico * 0.4
        alumno.nota_final = nota_parciales + nota_practico

def clasificar_alumnos(lista_alumnos):
    aprobados = []
    suspendidos = []

    for alumno in lista_alumnos:
        if alumno.asistencia >= 75 and alumno.parcial1 >= 4 and alumno.parcial2 >= 4 and alumno.practico >= 4 and alumno.nota_final >= 5:
            aprobados.append(alumno)
        else:
            suspendidos.append(alumno)

    return aprobados, suspendidos
