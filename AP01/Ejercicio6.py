# Escribe un programa que determine si un alumno puede o no aprobar el curso en convocatoria ordinaria, según si ha suspendido, o no,
# la primera, la segunda y la tercera evaluación, y teniendo en cuenta que es posible aprobar el curso con la primera evaluación suspendida. La información de aprobado o suspenso en cada evaluación se le solicita al usuario como entrada.

# Borramos la pantalla
from os import system
system("cls")

print("Introduce las notas de 2º DAM de SGE")
sge1 = float(input("Introduce la nota de la primera evaluacion: "))
sge2 = float(input("Introduce la nota de la segunda evaluacion: "))
sge3 = float(input("Introduce la nota de la tercera evaluacion: "))

if (sge1 >= 5 and sge2 >= 5 and sge3 >= 5):
    print("\nEl alumno esta aprobado en convocatoria ordinaria.")
elif (sge2 >= 5 and sge3 >= 5):
    print("\nEl alumno esta aprobado en convocatoria ordinaria, aunque tenga la primera evaluacion suspendida.")
else:
    print("\nEl alumno no esta aprobado en convocatoria ordinaria, tendra que presentarse a la convocatoria extraordinaria.")
