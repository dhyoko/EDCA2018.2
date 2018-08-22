'''
@Diogo Hitoshi Yokoyama
Atividade 1 - EDCA - 23 08 18 - Insertion Sort
'''

import sys
import numpy as np
import time

if len(sys.argv) != 2:
    print("\nError!")
    sys.exit(1)

n = int(open(str(sys.argv[1])).readline())
data = np.loadtxt(str(sys.argv[1]))

f = open('rIS' + str(sys.argv[1]) + ".txt", "a+")

start = time.clock()

for i in range(1, n + 1):
    aux = data[i]
    j = i -1
    while j >= 0 and data[j] > aux:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = aux

end = time.clock()

print(data)

print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")

f.write(str(sys.argv[1]) + " " + "{0:.8f}".format(end - start) + "\n")
f.close()