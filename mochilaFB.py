from archivo import Archivo

class MochilaFB:

    pesomaximo = 0
    peso=[]
    valor=[]
    nombre_archivo = ""
    def __init__(self, nombre_archivo):
        info = Archivo.leer_archivo_mochila(nombre_archivo)
        self.pesomaximo = info[0]
        self.peso = info[1]
        self.valor = info[2]
        self.nombre_archivo = nombre_archivo



    #Returns the maximum value that can be stored by the bag
    def knapSack(self,n, W,wt, val):
       # initial conditions
       if n == 0 or W == 0 :
          return 0
       # If weight is higher than capacity then it is not included
       if (wt[n-1] > W):
          return self.knapSack(n-1,W, wt, val)
       # return either nth item being included or not
       else:
          return max(val[n-1] + self.knapSack(n-1,W-wt[n-1], wt, val), self.knapSack(n-1,W, wt, val))

