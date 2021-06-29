import numpy as np
case = int(input())
layers = []
for test in range(case):
    layers.append(int(input()))
for layer in layers:
    row = 2+(4*(layer-1))
    col = row
    arr = np.zeros(row*col).reshape(row,col)
    #print(arr)
    for sec in range(layer):
        for i in range(2*sec,row-(2*sec)):
            for j in range(2*sec,col-(2*sec)):
                if i == 2*sec or i == row-(2*sec)-1 or j == 2*sec or j == col-(2*sec)-1:
                    arr[i,j]=1
    row,col = arr.shape
    for i in range(row):
        for j in range(col):
            if arr[i,j] == 1:
                print('*', end = '  ')
            else:
                print(' ', end = '  ')
        print('\n')
    