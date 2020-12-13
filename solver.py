import sys
from mochilaDinamica import MochilaPD
from AlineamientoDinamico import AlineamientoDinamico
from mochilaFB import MochilaFB


def main(argv):

    #mochila = MochilaPD(argv[0])
    #print(mochila.knapsack(len(mochila.peso),mochila.pesomaximo,mochila.peso,mochila.valor))
    #alineamiento = AlineamientoDinamico(argv[0])
    #print(alineamiento.needleman_wunsch1(alineamiento.seq1, alineamiento.seq2))
    mochila = MochilaFB(argv[0])
    print(mochila.knapSack(len(mochila.peso),mochila.pesomaximo,mochila.peso,mochila.valor))
if __name__ == '__main__':
    main(sys.argv[1:])
    
