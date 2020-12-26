#Promedio_Notas
suma = 0
notaL = []
print("Promedio de Notas")
print("Cuantas Notas deseas ingresa: ")
nNotas = input()
print("Ingresó " + nNotas + " notas es correcto Si/No")
respB = input()

if respB == "Si":  
    for rec in range(int(nNotas)):
        rec+=1
        nota=float(input("Ingresa nota nº"+ str(rec) + ": "))
        notaL.append(nota)
        

print("Tus notas son las siguientes: ")
print(notaL)
print("Tu nota mas alta es: ")
print(max(notaL))
print("Tu nota mas baja es: ")
print(min(notaL))
promedio = sum(notaL)/int(nNotas)
if promedio > 14:
    print("El promedio de las notas es: " + str(promedio) +" Estas APROBADO")
else:
    print("El promedio de las notas es: " + str(promedio) +" Estas DESAPROBADO")