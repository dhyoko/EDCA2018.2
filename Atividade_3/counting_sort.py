'''
@Diogo Hitoshi Yokoyama
Atividade 2 - EDCA - 11 09 18 - Counting Sort
'''

import sys
import numpy as np
import time

def countingSort(a):

    am = abs(min(a))
    k = max(a) + 1 + am
    c = [0]*k
    n = len(a)
    b = [0]*n

    for i in range(0, n):
        c[a[i] + am] += 1
    
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]

    for i in range(0, n):
        b[int(c[a[n - i - 1] + am]) - 1] = a[n - i - 1]
        c[a[n - i - 1] + am] -= 1

    for i in range(0, n):
        a[i] = b[i]

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("\nError!")
        sys.exit(1)

    n = int(open(str(sys.argv[1])).readline())
    data = np.loadtxt(str(sys.argv[1])).astype(int)

    start = time.clock()

    countingSort(data)

    end = time.clock()

    print(data)

    print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")
    