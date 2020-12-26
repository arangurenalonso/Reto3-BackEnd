numnotas = input(int('Ingrese la cantidad de notas que desea ingresar al sistema'))

while True
    try:
            comprobador = numnotas / 2
            break
    except ValueError as e:
            print('Por favor Ingrese un número')
        

Listanotas = []
listanotas2 = []

for i in numnotas:
    nombre = input('Ingrese el nombre del alumno')
    nota = input(int('Ingrese la nota del alumno'))
    dict = {'Nombre' : nombre, 'Nota' : nota)
    Listanotas.append(dict) 
    Listanotas2.append(nota)
    i += 1

notamayor = max(listanotas2)
notamenor = min(listanotas2)
sumatorianotas = sum(listanotas2)
Nnotas = int(len(listanotas2))
notapromedio = sumatorianotas/Nnotas
print(f'La nota mayor es {notamayor}')
print(f'La nota menor es {notamenor}')
print(f'La nota promedio es {notapromedio}')
 
notabuscada = input(int('Ingrese la nota a buscar'))

while True
    try:
            comprobador2 = numnotas / 2
            break
    except ValueError as z:
            print('Por favor Ingrese un número')
        

nombresconnotas[]

for notabuscada in listanotas2:
    matchnombre = listanotas2.get('Nombre')
    nombresconnotas.append(matchnombre)






