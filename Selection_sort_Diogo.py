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

f = open('rSS' + str(sys.argv[1]) + ".txt", "a+")

start = time.clock()

for i in range(0, n+1):
    min = i
    for j in range(i+1, n+1):
        if data[j] < data[min]:
            min = j
    if data[i] != data[min]:
        aux = data[i]
        data[i] = data[min]
        data[min] = aux

end = time.clock()

print(data)

print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")

f.write(str(sys.argv[1]) + " " + "{0:.8f}".format(end - start) + "\n")
f.close()