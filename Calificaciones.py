# INGRESAR CALIFICACION
calificaciones = []
for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    calificaciones.append(calificacion)

# CALCULAR PROMEDIO
promedio = sum(calificaciones) / len(calificaciones)

# ESTADO ESTUDIANTE
if promedio >= 60:
    estado = "Aprobado"
elif 40 <= promedio < 60:
    estado = "En recuperación"
else:
    estado = "Reprobado"

# IMPRIMIR RESULTADO
print(f"El promedio es: {promedio}")
print(f"Estado: {estado}")

