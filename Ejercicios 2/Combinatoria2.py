import itertools
def combinatoria2(set,num_combinaciones):
    referencias = itertools.combinations(set, num_combinaciones)
    lista_referencia = []    
    for elemento in referencias:
        lista_referencias.append(elemento)  
    print (lista_referencias)
