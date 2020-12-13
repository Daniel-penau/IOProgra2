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
    
    # Here is a helper function to print out matrices
    def print_matrix(self,mat):
        # Loop over all rows
        for i in range(0, len(mat)):
            print("[", end = "")
            # Loop over each column in row i
            for j in range(0, len(mat[i])):
            # Print out the value in row i, column j
                print(mat[i][j], end = "")
                # Only add a tab if we're not in the last column
                if j != len(mat[i]) - 1:
                    print("\t", end = "")
            print("]\n")


    

    # A function for making a matrix of zeroes
    def zeros(self,rows, cols):
        # Define an empty list
        retval = []
        # Set up the rows of the matrix
        for x in range(rows):
            # For each row, add an empty list
            retval.append([])
            # Set up the columns in each row
            for y in range(cols):
                # Add a zero to each column in each row
                retval[-1].append(0)
        # Return the matrix of zeros
        return retval

    # A function for determining the score between any two bases in alignment
    def match_score(self,alpha, beta):
        if alpha == beta:
            return self.match
        elif alpha == '_' or beta == '_':
            return self.gap
        else:
            return self.missmatch

    # The function that actually fills out a matrix of scores
    def needleman_wunsch(self,seq1, seq2):
    
        # length of two sequences
        n = len(seq1)
        m = len(seq2)  
    
        # Generate matrix of zeros to store scores
        score = self.zeros(m+1, n+1)
   
        # Calculate score table
    
        #Your code goes here
    
        # Fill out first column
        for i in range(0, m + 1):
           score[i][0] = self.gap * i
    
        # Fill out first row
        for j in range(0, n + 1):
            score[0][j] = self.gap * j
    
        # Fill out all other values in the score matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the score by checking the top, left, and diagonal cells
                match = score[i - 1][j - 1] + self.match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + self.gap
                insert = score[i][j - 1] + self.gap
                # Record the maximum score from the three possible scores calculated above
                score[i][j] = max(match, delete, insert)

        return score

    #print_matrix(needleman_wunsch(seq1, seq2))



    def needleman_wunsch1(self,seq1, seq2):
    
        # Store length of two sequences
        n = len(seq1)  
        m = len(seq2)
    
        # Generate matrix of zeros to store scores
        score = self.zeros(m+1, n+1)
   
        # Calculate score table
    
        # Fill out first column
        for i in range(0, m + 1):
            score[i][0] = self.gap * i
    
        # Fill out first row
        for j in range(0, n + 1):
            score[0][j] = self.gap * j
    
        # Fill out all other values in the score matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Calculate the score by checking the top, left, and diagonal cells
                match = score[i - 1][j - 1] + self.match_score(seq1[j-1], seq2[i-1])
                delete = score[i - 1][j] + self.gap
                insert = score[i][j - 1] + self.gap
                # Record the maximum score from the three possible scores calculated above
                score[i][j] = max(match, delete, insert)
    
        # Traceback and compute the alignment 
    
        # Create variables to store alignment
        align1 = ""
        align2 = ""
    
        # Start from the bottom right cell in matrix
        i = m
        j = n
    
        # We'll use i and j to keep track of where we are in the matrix, just like above
        while i > 0 and j > 0: # end touching the top or the left edge
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
        
            # Check to figure out which cell the current score was calculated from,
            # then update i and j to correspond to that cell.
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

        # Finish tracing up to the top left cell
        while j > 0:
            align1 += seq1[j-1]
            align2 += '_'
            j -= 1
        while i > 0:
            align1 += '_'
            align2 += seq2[i-1]
            i -= 1
    
        # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
        # These two lines reverse the order of the characters in each sequence.
        align1 = align1[::-1]
        align2 = align2[::-1]
    
        return(align1, align2)

    #output1, output2 = needleman_wunsch(seq1, seq2)

    #print(output1 + "\n" + output2)
