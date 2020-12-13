from archivo import Archivo


class MochilaPD:

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
        
    
    def find_opt(self,i, c, M, values, items, weights):
        if i <= 0 or c <= 0:
            return items

        if (M[i - 1][c] >= (values[i - 1] + M[i - 1][c - weights[i - 1]])) or (c - weights[i - 1]) < 0:
            self.find_opt(i - 1, c, M, values, items, weights)

        else:
            items.append(i - 1)
            self.find_opt(i - 1, c - weights[i - 1], M, values, items, weights)


    def knapsack(self,n, C, weights, values):
    # Initialization of matrix of size (n*W)
        M = [[None for i in range(C + 1)] for j in range(len(values) + 1)]

        for c in range(C + 1):
            M[0][c] = 0

        for i in range(len(weights) + 1):
            M[i][0] = 0

        for i in range(1, n + 1):
            for c in range(1, C + 1):
                # If current weight exceeds capacity then we cannot take it
                if weights[i - 1] > c:
                    M[i][c] = M[i - 1][c]

                # Else we can take it, then find what gives us the optimal value, either
                # taking it or not taking it and we consider what gives us max value of those
                else:
                    M[i][c] = max(M[i - 1][c], values[i - 1] + M[i - 1][c - weights[i - 1]])
        items = []

        self.find_opt(n, C, M, values, items, weights)

        return M[n][C], items[::-1]
    


