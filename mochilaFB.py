from archivo import Archivo

class MochilaFB:

    pesomaximo = 0
    peso=[]
    valor=[]
    nombre_archivo = ""

    def __init__(self, nombre_archivo):
        info = Archivo.leer_archivo_mochila(nombre_archivo)
        self.pesomaximo = info[0]
        self.items = info[1]
        self.nombre_archivo = nombre_archivo



    def peso_total(self,items):
        return sum(x.weight for x in items)


    def valor_total(self,items):
        return sum(x.value for x in items)


    def mochila(self,items, peso_maximo):
        res = max(self.fuerza_bruta(items, peso_maximo), key=self.valor_total)
        return [sum(item.value for item in res), [item.id for item in res]]


    def fuerza_bruta(self,items, peso_maximo):
        aux = [p for p in items if p.weight <= peso_maximo]

        res = []

        for p in aux:
            fb = self.fuerza_bruta([x for x in aux if x != p], peso_maximo - p.weight)

            if len(fb) == 0:
                res.append([p])
            else:
                res.extend([[p] + x for x in fb])

        return res
       

