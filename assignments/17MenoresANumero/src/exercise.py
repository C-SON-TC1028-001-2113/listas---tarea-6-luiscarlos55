def resultados(m):
    listatotal=[]
    for i in range(len(m)):
        if m[i]<10:
            listatotal.append(m[i])
    return listatotal
def datos(a,b):
    valores=[]
    matriz=[]
    listatotal2=[]
    for i in range(a):
        for i in range(b):    
            valor=int(input())
            valores.append(valor)
        matriz.append(valores)
        listatotal2=listatotal2+valores
        valores=[]
        
    return resultados(listatotal2)
def main():
    r=int(input())
    c=int(input())
    print (datos(r,c))

if __name__=='__main__':
    main()

   



