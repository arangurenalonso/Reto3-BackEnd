try:
    lista = []
    for i in range (5):
        lista.append(int(input('Por favor coloque la nota 1\n')))
        lista.append(int(input('Por favor coloque la nota 2\n')))
        lista.append(int(input('Por favor coloque la nota 3\n')))
        lista.append(int(input('Por favor coloque la nota 4\n')))
        lista.append(int(input('Por favor coloque la nota 5\n')))
        break
        
        print (lista)
except Exception as e:
    print('Ocurrio un problema : {str(e)}')
finally:
    print('Se termino la ejecucion')
    print (lista)
    maximo=max(lista)
    minimo=min(lista)
    promedio=sum(lista)/len(lista)
    print(f'Nota media es {promedio}, la nota maxima es {maximo}, y la minima es {minimo}')