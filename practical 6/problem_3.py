

X = [[8 , 6 , 1] ,
    [4 , 5 , 1] ,
    [6 , 2 , 2]]
    
Y = [[1 , 2 , 2],
    [4 , 9 , 1],
    [3 , 6 , 5]]

#result is 3 x 4

result = [[sum(a * b for a , b in zip (X_row , Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
    print(r)
    