def LevenshteinDistance_Recursive(s, t):
    if   s == "": return len(t)
    elif t == "": return len(s)

    cost = 0 if s[-1] == t[-1] else 1
       
    return min(
        [
            LevenshteinDistance_Recursive(s[:-1], t)+1,
            LevenshteinDistance_Recursive(s, t[:-1])+1, 
            LevenshteinDistance_Recursive(s[:-1], t[:-1]) + cost
        ]
    )

def LevenshteinDistance_Iterative(s, t, deleteCost=1, insertCost=1, substituteCost=1):
    # create matrix
    rows, cols = len(s)+1, len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # setup delete cost column and insert cost array
    for i in range(1, rows): dist[i][0] = i*deleteCost
    for i in range(1, cols): dist[0][i] = i*insertCost
        
    # perform interation
    for col in range(1, cols):
        for row in range(1, rows):
            cost = 0 if s[row-1] == t[col-1] else substituteCost
            dist[row][col] = min(
                dist[row-1][col]   + deleteCost,  # deletion
                dist[row][col-1]   + insertCost,  # insertion
                dist[row-1][col-1] + cost)        # substitution

    #for r in dist: print(r)
    return dist[row][col]

print(LevenshteinDistance_Recursive("Python", "Peithen"))
print(LevenshteinDistance_Iterative("Python", "Peithen"))