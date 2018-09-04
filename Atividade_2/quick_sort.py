'''
@Diogo Hitoshi Yokoyama
Atividade 2 - EDCA - 04 09 18 - Quick Sort
'''

import sys
import numpy as np
import time


def partition(A, e, d):
    i = e - 1          
    pivo = A[d]     
 
    for j in range(e , d):
 
        if   A[j] <= pivo:
        
            i = i + 1
            A[i], A[j] = A[j], A[i]
 
    A[i + 1], A[d] = A[d], A[i + 1]
    return ( i + 1 )
 
    
def quicksort(A, e, d):
    if e < d:
 
        pivo_i = partition(A, e, d)
         
        quicksort(A, e, pivo_i - 1)
        quicksort(A, pivo_i + 1, d)
        
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("\nError!")
        sys.exit(1)
    n = int(open(str(sys.argv[1])).readline())
    data = np.loadtxt(str(sys.argv[1]))

    start = time.clock()
    
    quicksort(data, 0, n)
    
    end = time.clock()
    
    print(data)
    
    print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")

    
