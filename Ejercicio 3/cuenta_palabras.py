import sys
import re
from operator import itemgetter
sys.setrecursionlimit(10000)

def cuenta(dicc):
    if (len(dicc) > 0):
        palabra2, cantidad = dicc.popitem()
        return cuenta(dicc) + cantidad
    else:
        return 0

def funes():
    f = open("funes.txt","r",encoding='utf-8')
    respaldo = f.read()
    respaldo=respaldo.lower()
    l = respaldo.split()
    dicc = {}
    dicc = dict.fromkeys(l,0)
    for palabra in l:
        if palabra in dicc:
            dicc[palabra]=int(dicc[palabra]+1)        
    print(" El texto tiene " , cuenta(dicc) , " palabras")
    f.close()
 

