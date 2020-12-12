# Here's how to make the matrix above from a list of lists
my_matrix = []
# Fill out the 0th row
my_matrix.append([1, 3, 5, 7])
# Fill out the 1st row
my_matrix.append([2, 3, 4, 5])
# Fill out the 2nd row
my_matrix.append([5, 2, 20, 3])

# Here is a helper function to print out matrices
def print_matrix(mat):
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

print_matrix(my_matrix)

# To retrieve the value from the 2nd row, in the 0th column, is relatively simple:
print("The value in the 2nd row and the 0th column is:", my_matrix[2][0])

# The format is always my_matrix[row][column]. 


# Use these values to calculate scores
gap_penalty = -1
match_award = 1
mismatch_penalty = -1

# Make a score matrix with these two sequences
seq1 = "ATTGTGATCC"
seq2 = "TTGCATCGGC"

# A function for making a matrix of zeroes
def zeros(rows, cols):
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
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '_' or beta == '_':
        return gap_penalty
    else:
        return mismatch_penalty

# The function that actually fills out a matrix of scores
def needleman_wunsch(seq1, seq2):
    
    # length of two sequences
    n = len(seq1)
    m = len(seq2)  
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Your code goes here
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(match, delete, insert)

    return score

print_matrix(needleman_wunsch(seq1, seq2))



def needleman_wunsch(seq1, seq2):
    
    # Store length of two sequences
    n = len(seq1)  
    m = len(seq2)
    
    # Generate matrix of zeros to store scores
    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    
    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
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
        if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[j-1]
            align2 += '_'
            j -= 1
        elif score_current == score_left + gap_penalty:
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

output1, output2 = needleman_wunsch(seq1, seq2)

print(output1 + "\n" + output2)
