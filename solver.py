import sys
import time
from mochilaDinamica import MochilaPD
from AlineamientoDinamico import AlineamientoDinamico
from mochilaFB import MochilaFB
from archivo import Archivo

# resuelve los experimentos
def main(argv):
    start = time.time()
    nombre_sol=Archivo.crearNombre(argv[0])
    #mochila = MochilaPD(argv[0])
    #print(mochila.mochila(mochila.items, mochila.pesomaximo))
    alineamiento = AlineamientoDinamico(argv[0])
    Archivo.crearArchivo(nombre_sol,alineamiento.needleman_wunsch(alineamiento.seq1, alineamiento.seq2))
    #mochila = MochilaFB(argv[0])
    #Archivo.crearArchivo(nombre_sol,mochila.mochila(mochila.items, mochila.pesomaximo))
    end=time.time()
    print(end-start)
if __name__ == '__main__':
    main(sys.argv[1:])
    
