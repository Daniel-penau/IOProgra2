from item import Item 

class Archivo:
#lee el archivo de entrada para mochila
    @staticmethod
    def leer_archivo_mochila(file_name):

        try:

            file = open(file_name, 'r')
            line_count = 0
            items =[]
            pesomaximo = -1
            i=0
            for line in file.readlines():
                line = line.strip("\n")
                line_splitted_by_comma = line.split(",")
                
                
               
                
                if line_count == 0:
                   
                    if line_splitted_by_comma[0].isnumeric():
                        pesomaximo = int(line_splitted_by_comma[0])
                        

                    else:
                        raise Exception("Error al procesar el  archivo")
                else:
                    i+=1
                    cantidad = int(line_splitted_by_comma[2])
                    while cantidad > 0:
                        item = Item(i,int(line_splitted_by_comma[0]),int(line_splitted_by_comma[1]))
                        items.append(item)
                       
                        cantidad -=1

                line_count += 1
            res = [pesomaximo, items]
            return res

        except:
            print("El archivo no existe o hay un error dentro del mismo.")
    #lee archivo de entrada para Alineamento de secuencias
    @staticmethod
    def leer_archivo_alineamiento(file_name):

        try:

            file = open(file_name, 'r')

            line_count = 0
            match=0
            missmatch =0
            gap = 0
            secuencia_1=""
            secuencia_2=""

            for line in file.readlines():
                line = line.strip("\n")
                line_splitted_by_comma = line.split(",")
               
                
                if line_count == 0:
                   i = 0 
                   while i < len(line_splitted_by_comma):
                       
                       strip = line_splitted_by_comma[i].strip('-')
                       if strip.isnumeric():
                           
                           if i == 0:
                              match = int(line_splitted_by_comma[i])
                              
                           elif i == 1:
                             
                              missmatch = int(line_splitted_by_comma[i])
                             
                           else:
                              gap =int(line_splitted_by_comma[i])
                         
                        
                       else:
                           raise Exception("Error al procesar el  archivo")
                       i += 1  
                elif line_count == 1:
                    secuencia_1 = line_splitted_by_comma[0]
                else:
                    secuencia_2 = line_splitted_by_comma[0]
                    

                line_count += 1
            res = [match, missmatch, gap, secuencia_1, secuencia_2]
            
            return res

        except:
            print("El archivo no existe o hay un error dentro del mismo.")

        

#crea el nombre del archivo solucion
    @staticmethod
    def crearNombre(nombre_archivo):
        archivo_solucion = nombre_archivo + '_solucion'
        return archivo_solucion
#crea el Archivo nuevo.
    @staticmethod
    def crearArchivo(nombre_archivo, contenido):
        try:
            archivo = open(nombre_archivo, 'w')
            archivo.write(str(contenido).strip('[]'))
            archivo.close()
        except:
            print("ERROR: El archivo no existe.")

    @staticmethod
    def is_digit(n):
        try:
            float(n)
        except ValueError:
            return False
        return True


