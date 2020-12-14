import sys
from mochilaDinamica import MochilaPD
from AlineamientoDinamico import AlineamientoDinamico
from mochilaFB import MochilaFB
from archivo import Archivo


def main(argv):

    #mochila = MochilaPD(argv[0])
    #print(mochila.mochila(mochila.items, mochila.pesomaximo))
    #alineamiento = AlineamientoDinamico(argv[0])
    #print(alineamiento.needleman_wunsch1(alineamiento.seq1, alineamiento.seq2))
    mochila = MochilaFB(argv[0])
    nombre_sol=Archivo.crearNombre(argv[0])
    Archivo.crearArchivo(nombre_sol,mochila.mochila(mochila.items, mochila.pesomaximo))

if __name__ == '__main__':
    main(sys.argv[1:])
    
