import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from alumno import Alumno
import calificaciones

def mostrar_alumnos_sin_orden(lista_alumnos, output_text):
    output_text.insert(tk.END, '--- Lista sin ordenar ---\n')
    for alumno in lista_alumnos:
        output_text.insert(tk.END, f'Nombre: {alumno.nombre}\n')
        output_text.insert(tk.END, f'Apellidos: {alumno.apellidos}\n')
        output_text.insert(tk.END, f'Parcial 1: {alumno.parcial1}\n')
        output_text.insert(tk.END, f'Parcial 2: {alumno.parcial2}\n')
        output_text.insert(tk.END, f'Práctico: {alumno.practico}\n')
        output_text.insert(tk.END, f'Asistencia: {alumno.asistencia}\n')
        output_text.insert(tk.END, '-------------------------\n')

def mostrar_alumnos_ordenados(lista_alumnos, output_text):
    output_text.insert(tk.END, '--- Lista ordenada por apellidos ---\n')
    for alumno in lista_alumnos:
        output_text.insert(tk.END, f'Nombre: {alumno.nombre}\n')
        output_text.insert(tk.END, f'Apellidos: {alumno.apellidos}\n')
        output_text.insert(tk.END, f'Parcial 1: {alumno.parcial1}\n')
        output_text.insert(tk.END, f'Parcial 2: {alumno.parcial2}\n')
        output_text.insert(tk.END, f'Práctico: {alumno.practico}\n')
        output_text.insert(tk.END, f'Asistencia: {alumno.asistencia}\n')
        output_text.insert(tk.END, '-------------------------\n')

def mostrar_aprobados_suspendidos(aprobados, suspendidos):
    messagebox.showinfo('Aprobados', f'Alumnos aprobados: {len(aprobados)}\n\nDetalles:\n\n' +
                        '\n'.join([f'{alumno.nombre} {alumno.apellidos}' for alumno in aprobados]))

    messagebox.showinfo('Suspendidos', f'Alumnos suspendidos: {len(suspendidos)}\n\nDetalles:\n\n' +
                        '\n'.join([f'{alumno.nombre} {alumno.apellidos}' for alumno in suspendidos]))

def mostrar_tablas(lista_alumnos):
    output_text = ScrolledText()
    output_text.pack(expand=True, fill='both')
    
    mostrar_alumnos_sin_orden(lista_alumnos, output_text)
    output_text.insert(tk.END, '\n')
    
    calificaciones.quicksort(lista_alumnos, 0, len(lista_alumnos) - 1)
    mostrar_alumnos_ordenados(lista_alumnos, output_text)

    output_text.configure(state='disabled')

def mostrar_nota_final(lista_alumnos):
    output_text = ScrolledText()
    output_text.pack(expand=True, fill='both')

    for alumno in lista_alumnos:
        output_text.insert(tk.END, f'Nombre: {alumno.nombre}\n')
        output_text.insert(tk.END, f'Apellidos: {alumno.apellidos}\n')
        output_text.insert(tk.END, f'Parcial 1: {alumno.parcial1}\n')
        output_text.insert(tk.END, f'Parcial 2: {alumno.parcial2}\n')
        output_text.insert(tk.END, f'Práctico: {alumno.practico}\n')
        output_text.insert(tk.END, f'Asistencia: {alumno.asistencia}\n')
        output_text.insert(tk.END, f'Nota final: {alumno.nota_final}\n')
        output_text.insert(tk.END, '-------------------------\n')

    output_text.configure(state='disabled')

def procesar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

    if archivo:
        lista_alumnos = calificaciones.cargar_calificaciones(archivo)

        # Mostrar tablas sin ordenar y ordenada por apellidos
        mostrar_tablas(lista_alumnos)

        # Calcular la nota final de cada alumno
        calificaciones.calcular_nota_final(lista_alumnos)

        # Mostrar la lista de alumnos aprobados y suspendidos
        aprobados, suspendidos = calificaciones.clasificar_alumnos(lista_alumnos)
        mostrar_aprobados_suspendidos(aprobados, suspendidos)

def main():
    window = tk.Tk()
    window.title('Programa de calificaciones')
    window.geometry('600x600')

    button = tk.Button(window, text='Seleccionar archivo', command=procesar_archivo)
    button.pack(pady=20)

    window.mainloop()
