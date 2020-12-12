def bestAlignment (U, V, c, g):  
    if len(U) == 0 or len(V) == 0:
        while len(U) < len(V): U = U + GAP
        while len(V) < len(U): V = V + GAP
        return U, V
    else:
        # try with no gap
        (U0, V0) = bestAlignment (U[1:], V[1:], c, g)
        scoreNoGap = goodnessScore (U0, V0, c, g)
        if U[0] == V[0]: scoreNoGap += c
        
        # try inserting a gap in U (no match for V[0])
        (U1, V1) = bestAlignment (U, V[1:], c, g)
        scoreGapU = goodnessScore (U1, V1, c, g) - g
        
        # try inserting a gap in V (no match for U[0])
        (U2, V2) = bestAlignment (U[1:], V, c, g)
        scoreGapV = goodnessScore (U2, V2, c, g) - g
        
        if scoreNoGap >= scoreGapU and scoreNoGap >= scoreGapV:
            return U[0] + U0, V[0] + V0
        elif scoreGapU >= scoreGapV:
            return GAP + U1, V[0] + V1
        else:
            return U[0] + U2, GAP + V2
