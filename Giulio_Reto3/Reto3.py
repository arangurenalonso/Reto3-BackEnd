while True:
    try:
            numnotas = int(input('Ingrese la cantidad de notas que desea ingresar al sistema\n'))
            break
    except ValueError as e:
            print('Por favor Ingrese un número')
        

Listanotas = []
listanotas2 = []

for i in range(0,numnotas,1):
    nombre = input('Ingrese el nombre del alumno\n')
    nota = int(input('Ingrese la nota del alumno\n'))
    dict = {'Nombre' : nombre, 'Nota' : nota}
    Listanotas.append(dict) 
    listanotas2.append(nota)
    i += 1

notamayor = max(listanotas2)
notamenor = min(listanotas2)
sumatorianotas = sum(listanotas2)
Nnotas = int(len(listanotas2))
notapromedio = sumatorianotas/Nnotas
print(f'La nota mayor es {notamayor}')
print(f'La nota menor es {notamenor}')
print(f'La nota promedio es {notapromedio}')
 



