def Tri_pascal(n):
    if n == 0:
        return 1
    else:
        Fila = [ ]
        for contador in range(n+1):
            if contador == 0 or contador == n :
                Fila = Fila + [1]
            else:
                Fila = Fila + [ Tri_pascal(n-1)[contador-1] + Tri_pascal(n-1)[contador]]
    return Fila
