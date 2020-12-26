while True:
        try:
            while True:
                cantNotasIngresar=int(input(f"Cantidad de notas a ingresar:\n"))
                if cantNotasIngresar>=0:
                    break
                else:
                    print("Ingrese un numero mayor a 0")
            break

        except ValueError:
            print(f'Ingrese un numero')

notas=[]

for i in range(0,cantNotasIngresar,1):
    while True:
        try:
            while True:
                nota=float(input(f"Ingrese la nota {i+1}:\n"))
                if nota>=0 and nota<=20:
                    dicionario=dict(nota=nota)
                    notas.append(dicionario)
                    break
                else:
                    print("Ingrese una nota entre 0 a 20")
            break

        except ValueError:
            print(f'Ingrese un numero valido')
suma=0
prom=0
numMax=-9999
numMin=9999


for nota in notas:
    if nota.get('nota')<numMin:
        numMin=nota.get('nota')
    
    if nota.get('nota')>numMax:
        numMax=nota.get('nota')
    
    suma+=nota.get('nota')

prom=suma/len(notas)
print(f'El promedio de las notas es: {prom}')

print(f'La nota mas alta es: {numMax}')

print(f'La nota mas baja es: {numMin}')

    