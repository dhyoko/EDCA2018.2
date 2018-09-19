"""
@Diogo Hitoshi Yokoyama
Atividade 4 - EDCA - 20 09 18 - Heap Sort

"""
import math as mt
import pdb

class heap:

    def __init__(self, A):
        self.data = A
        self.comprimento = len(A)
        self.tamanho = self.comprimento

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def parent(self, i):
        return mt.floor(i)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def __setitem__(self, key, item):
        self.data[key] = item

    def __getitem__(self, key):
        return self.data[key]

    def maxHeapfy(A, i):
        l = A.left(i)
        r = A.right(i)

        if l < A.tamanho and A[l] > A[i]:
            maior = l
        else:
            maior = i

        if r < A.tamanho and A[r] > A[maior]:
                maior = r

        if maior != i:
            A[i], A[maior] = A[maior], A[i]
            A.maxHeapfy(maior)

    def build_max_heap(self):
        self.tamanho = self.comprimento
        for i in range(mt.floor(self.comprimento/2)-1, -1, -1):
            self.maxHeapfy(i)

    def heapsort(self):
        self.build_max_heap()
        for i in range(self.comprimento-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.tamanho = self.tamanho - 1
            self.maxHeapfy(0)

if __name__=="__main__":
    a = heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    a.heapsort()
    print(a)
