def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    n=int(numero)
    l=list()
    while n!=0:
        r=n%2
        l.append(r)
        n=n//2
    l.reverse()
    for element in l:
        print(element,end="")
    return l
NumeroBinario(78)

