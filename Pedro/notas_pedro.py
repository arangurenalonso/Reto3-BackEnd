lista=[]
try:
    for i in range (1,5,1):
        lista.append(int(input(f'Por favor coloque la nota {i}\n')))
        break
except Exception as e:
    e.__class__.__name__
    print(f'Ocurrio un problema : {str(e)}')
finally:
    print('Se termino la ejecucion')


print(lista)
maximo=max(lista)
minimo=min(lista)
promedio=sum(lista)/len(lista)
print(f'Nota media es {promedio}, la nota maxima es {maximo}, y la minima es {minimo}')