class Alumno:
    def __init__(self, nombre, apellidos, parcial1, parcial2, practico, asistencia):
        self.nombre = nombre
        self.apellidos = apellidos
        self.parcial1 = float(parcial1)
        self.parcial2 = float(parcial2)
        self.practico = float(practico)
        self.asistencia = int(asistencia)
        self.nota_final = None
