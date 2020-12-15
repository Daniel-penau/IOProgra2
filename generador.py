import sys
import random
from archivo import Archivo


# genera experimentos
def main(argv):
    contenido =""
    id_problema = argv[0]
    if len(argv) == 9:
        W = argv[1]
        N = int(argv[2])
        contenido += W
        while N > 0:
           minPeso = argv[3]
           maxPeso = argv[4]
           minBeneficio = argv[5]
           maxBeneficio = argv[6]
           minCantidad = argv[7]
           maxCantidad = argv[8]
           peso = random.randint(int(minPeso), int(maxPeso))
           beneficio = random.randint(int(minBeneficio), int(maxBeneficio))
           cantidad = random.randint(int(minCantidad),int(maxCantidad))
           contenido += '\n' + str(peso) + ',' + str(beneficio) + ',' + str(cantidad)
           N-=1
        Archivo.crearArchivo(id_problema,contenido)
    elif len(argv) == 3:
        contenido +="1,-1,-2"+ '\n' + argv[1] + '\n'+ argv[2]
        
    else:
    	print("Parametro insuficientes")
    Archivo.crearArchivo(id_problema,contenido)
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
    
