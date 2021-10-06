def main():
    lista=[]
    numero=-1
    while numero<0:
        numero=int(input())
    if numero==0:
        print('[]')
    elif numero>0:
        lista=[0,1]
        if numero>2:
            for i in range(numero-2):
                lista.append(lista[i]+lista[i+1])
            print(lista)
        elif numero==1:
            print('[0]')
        elif numero==2:
            print(lista)

if __name__=='__main__':
    main()
