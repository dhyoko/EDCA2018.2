'''
@Diogo Hitoshi Yokoyama
Atividade 2 - EDCA - 04 09 18 - Merge Sort
'''

import sys
import numpy as np
import time

def mergesort(A):
    Merge_Sort(A, 0, len(A) - 1)
    
def Merge_Sort(A, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        Merge_Sort(A, ini, meio)
        Merge_Sort(A, meio + 1, fim)
        merge(A, ini, meio, fim)
        
def merge(A, ini, meio, fim):
    n1 = meio - ini + 1
    n2 = fim - meio
    e = np.zeros(n1 + 1)
    d = np.zeros(n2 + 1)
    
    for i in range(0, n1):
        e[i] = A[ini + i]
    for j in range(0, n2):        
        d[j] = A[meio + j + 1]
    
    i = j = 0
    k = ini
    
    while i < n1 and j < n2 : 
        if e[i] <= d[j]: 
            A[k] = e[i] 
            i += 1
        else: 
            A[k] = d[j] 
            j += 1
        k += 1
    
    while i < n1: 
        A[k] = e[i] 
        i += 1
        k += 1
        
    while j < n2: 
        A[k] = d[j] 
        j += 1
        k += 1
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nError!")
        sys.exit(1)
    n = int(open(str(sys.argv[1])).readline())
    data = np.loadtxt(str(sys.argv[1]))

    start = time.clock()
    
    mergesort(data)
    
    end = time.clock()
    
    print(data)
    
    print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")

    