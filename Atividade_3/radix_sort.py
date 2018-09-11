'''
@Diogo Hitoshi Yokoyama
Atividade 2 - EDCA - 11 09 18 - Radix Sort
'''

import sys
import numpy as np
import time


def sign(x):
    if x == 0:
        return 0
    else:
        return int(x/abs(x))

def countingSort(a, exp):

    c = [0]*19
    n = len(a)
    b = [0]*n
    
    for i in range(0, n):
        index = a[i] // exp
        c[(abs(index) % 10)*sign(a[i]) + 9] += 1

    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]

    for i in range(0, n):
        index = a[n - i - 1] // exp
        b[int(c[(abs(index) % 10)*sign(a[n - i - 1]) + 9]) - 1] = a[n - i - 1]
        c[(abs(index) % 10)*sign(a[n - i - 1]) + 9] -= 1

    for i in range(0, n):
        a[i] = b[i]

def radixSort(a):
    digits = max(a, key=abs)
    exp = 1
    
    while digits // exp > 0:
        countingSort(a, exp)
        exp *= 10

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("\nError!")
        sys.exit(1)

    n = int(open(str(sys.argv[1])).readline())
    data = np.loadtxt(str(sys.argv[1])).astype(int)

    start = time.clock()

    radixSort(data)

    end = time.clock()

    print(data)

    print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")

    