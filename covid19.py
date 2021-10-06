import numpy as np

T = int(input())
for _ in range(T):
    inlst = input().split()
    N = int(inlst[0])
    M = int(inlst[1])
    entries = []
    
    for _ in range(N): 
        row = list(map(int, input().split()))
        entries.append(row)
    
    matrix = np.array(entries).reshape(N,M)
    
    countcycles = 0
    
    while True:
        listzeroes = []
        allzeroes = True
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    listzeroes.append([i,j])
                else:
                    allzeroes = False
        
        if allzeroes:
            break
                
        for pair in listzeroes:
            i = pair[0]
            j = pair[1]
            if i > 0:
                matrix[i-1][j] = 0
            if i < N-1:
                matrix[i+1][j] = 0
            if j > 0:
                matrix[i][j-1] = 0
            if j < M-1:
                matrix[i][j+1] = 0
                
        countcycles += 1
            
    
    print(countcycles)


