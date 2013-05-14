from operator import itemgetter
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
    dicc = sorted(dicc.items(),key=itemgetter(1),reverse=True)
    for palabra in dicc:
        print(palabra)
    f.close()
 
funes()
