from archivo import Archivo
from item import Item 

class MochilaPD:

    pesomaximo = 0
    items=[]
    nombre_archivo = ""
    def __init__(self, nombre_archivo):
        info = Archivo.leer_archivo_mochila(nombre_archivo)
        print(info[0])
        self.pesomaximo = info[0]
        self.items = info[1]
        self.nombre_archivo = nombre_archivo
        
    
    def mochila(self,items, peso_maximo):

       matriz = []
       n = len(items)

       for x in range(n):
           matriz.append([])
           for y in range(peso_maximo + 1):
               matriz[x].append(0)

       for i in range(n):
            for j in range(peso_maximo + 1):
                if items[i].weight < j+1:
                    matriz[i][j] = max(matriz[i-1][j], items[i].value + matriz[i-1][j - items[i].weight])
                else:
                    matriz[i][j] = matriz[i-1][j]

       res = [item.id for item in self.bottom_up(items, matriz)]

       return [matriz[n-1][peso_maximo], res]


    def bottom_up(self,items, matriz):

       row = len(matriz) - 1
       col = len(matriz[0]) - 1

       res = []

       while row > -1:

           if row == 0 and items[row].weight <= col:
               res.append(items[row])
               break

           if matriz[row][col] != matriz[row-1][col]:
               res.append(items[row])

               col -= items[row].weight

           row -= 1

       return res

    


