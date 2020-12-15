from archivo import Archivo


class AlineamientoDinamico:
    
    
    match = 0
    mismatch = 0
    gap = 0
    seq1 = ""
    seq2 = ""
    nombre_archivo = ""
    
    def __init__(self, nombre_archivo):
        info = Archivo.leer_archivo_alineamiento(nombre_archivo)
        self.match = info[0]
        self.missmatch = info[1]
        self.gap = info[2]
        self.seq1 = info[3]
        self.seq2 = info[4]
        self.nombre_archivo = nombre_archivo
    
    # imprime la matriz
    def print_matriz(self,mat):
        
        for i in range(0, len(mat)):
            print("[", end = "")
           
            for j in range(0, len(mat[i])):
           
                print(mat[i][j], end = "")
             
                if j != len(mat[i]) - 1:
                    print("\t", end = "")
            print("]\n")


    

    #Fucnion que crea matriz de zeros
    def zeros(self,rows, cols):
       
        retval = []
       
        for x in range(rows):
         
            retval.append([])
        
            for y in range(cols):
               
                retval[-1].append(0)
     
        return retval

    # A funcion que determina el valor de los score
    def match_score(self,alpha, beta):
        if alpha == beta:
            return self.match
        elif alpha == '_' or beta == '_':
            return self.gap
        else:
            return self.missmatch

    # Funcion que crea y llena la matriz
    def needleman_wunsch_mat(self,seq1, seq2):
    
        
        n = len(seq1)
        m = len(seq2)  
    
        # Genera matriz de zeros
        score = self.zeros(m+1, n+1)
   
        
        for i in range(0, m + 1):
           score[i][0] = self.gap * i
    
      
        for j in range(0, n + 1):
            score[0][j] = self.gap * j
    
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                match = score[i - 1][j - 1] + self.match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + self.gap
                insert = score[i][j - 1] + self.gap
                # revisa los score maximo
                score[i][j] = max(match, delete, insert)

        return score



    #Funcion que busca el maximo scor y el alineamiento
    def needleman_wunsch(self,seq1, seq2):
    
        
        n = len(seq1)  
        m = len(seq2)
    
        
        score = self.zeros(m+1, n+1)
   
        
        for i in range(0, m + 1):
            score[i][0] = self.gap * i
    
        
        for j in range(0, n + 1):
            score[0][j] = self.gap * j
    
        # revisa los valores de la tabla con los score
        for i in range(1, m + 1):
            for j in range(1, n + 1):
               
                match = score[i - 1][j - 1] + self.match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + self.gap
                insert = score[i][j - 1] + self.gap
                # muestra el score maximo
                score[i][j] = max(match, delete, insert)
    

       
        align1 = ""
        align2 = ""
    
        
        i = m
        j = n
    

        while i > 0 and j > 0:
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
        
           
            if score_current == score_diagonal + self.match_score(seq1[j-1], seq2[i-1]):
                align1 += seq1[j-1]
                align2 += seq2[i-1]
                i -= 1
                j -= 1
            elif score_current == score_up + self.gap:
                align1 += seq1[j-1]
                align2 += '_'
                j -= 1
            elif score_current == score_left + self.gap:
                align1 += '_'
                align2 += seq2[i-1]
                i -= 1

       
        while j > 0:
            align1 += seq1[j-1]
            align2 += '_'
            j -= 1
        while i > 0:
            align1 += '_'
            align2 += seq2[i-1]
            i -= 1
    
       
        # le da vuelta a la secuencia ya que la revisamos alreves.
        align1 = align1[::-1]
        align2 = align2[::-1]
        matriz_final = self.needleman_wunsch_mat(seq1,seq2)
        return(matriz_final,score[n][m],align1, align2)

