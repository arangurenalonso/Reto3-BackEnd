
notas=[]

for i in range(0,5,1):
    while True:
        try:
            while True:
                nota=float(input(f"Ingrese la nota {i+1}:\n"))
                if nota>=0 and nota<=20:
                    notas.append(nota)
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
    if nota<numMin:
        numMin=nota
    
    if nota>numMax:
        numMax=nota
    
    suma+=nota

prom=suma/len(notas)
print(f'El promedio de las notas es: {prom}')

print(f'La nota mas alta es: {numMax}')

print(f'La nota mas baja es: {numMin}')

    



     
