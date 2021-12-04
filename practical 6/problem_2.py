

X = [[18 , 16 , 12] ,
    [4 , 9 , 10] ,
    [6 , 23 , 52]]
    
Y = [[10 , 6 , 2],
    [14 , 19 , 1],
    [13 , 3 , 5]]
    
result = [[0 , 0 , 0],
         [0 , 0 , 0],
         [0 , 0 , 0]]
         
for i in range (len(X)):
    
    #interate through columns
    
    for k in range (len(X[0])):
        result[i] [k] = X[i] [k] + Y[i] [k]

for n in result:
    print(n)
    


    
    
    
    
