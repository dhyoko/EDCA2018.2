'''
@Diogo Hitoshi Yokoyama
Projeto final - Coloracao de grafos - Etapa 2
'''
import numpy as np
import copy
from collections import defaultdict
import time
import sys

def ler_instancia(nome):
    instancia = open(nome)
    x = defaultdict(list)
    for line in instancia:
        l_split = line.split()
        if l_split[0] == "p":           #numero de vertices
            v = int(l_split[-2])
        elif l_split[0] == "e":         #arestas
            x[int(l_split[1])].append(int(l_split[2]))
            x[int(l_split[2])].append(int(l_split[1]))
    return v, x

class grafo_cor:
    e = {}
    
    def __init__(self,v,e):
       self.v = v + 1
       self.e = e
       self.c = -1*np.ones(self.v).astype(int)
       self.k = 1
       self.h_construcao()
       #for i in range(0,10):
       self.cor_ls()
       
    def ord_grau(self):        #ordena pelo grau do vertice
        p = []
        for i in self.e:
           p.append([len(self.e[i]),i])
        p.sort(reverse = True)
        return p
    
    def min_color(self, x, y):
        n = np.ones(self.k)     # vetor cores usadas
        a = b = 0               # variaveis auxiliares
        for i in self.e[y]:     # verticies adjacentes
            if self.c[i] != -1 and n[self.c[i]] != 0: 
                n[self.c[i]] = 0
                b += 1
            elif self.c[i] == -1:
                a += 1
        if a == x:
            self.c[y] = 0
        elif b == self.k:
            self.k += 1
            self.c[y] = self.k - 1
        else:
            for i in range(0, len(n)):
                if n[i] == 1:
                    self.c[y] = i
                    break
    
    def h_construcao(self):
        p = self.ord_grau()
        self.l_cor = defaultdict(list)
        for x,y in p:
            self.min_color(x,y)
            self.l_cor[self.c[y]].append(y)
        self.cmax, check = self.eval_cor()
    
    def eval_cor(self):
        cmax = 0
        for i in self.e:
            if self.c[i] > cmax:
                cmax = self.c[i]
            for j in self.e[i]:
                if self.c[i] == self.c[j]:
                    return cmax, 0
        return cmax, 1
        
    def cor_ls(self):
        #print("Num. de Cores = " + str(self.k))
        #for i in range(0,self.k):
        #    print(str(i) + ":" + str(self.l_cor[i]))
        for a in self.l_cor:
            self.k_ = self.k - 1
            self.l_cor_ = copy.deepcopy(self.l_cor)
            for i in range(a,self.k - 1):
                self.l_cor_[i] = self.l_cor_[i + 1]
            del self.l_cor_[self.k - 1]
            self.c_ = self.c.copy()
            for i in range(0,len(self.c_)):
                if self.c_[i] > a:
                    self.c_[i] -= 1
            for y in self.l_cor[a]:
                self.c_[y] = -1
            for y in self.l_cor[a]:
                self.min_color_ls(y)
                self.l_cor_[self.c_[y]].append(y)
            cmax_, check_ = self.eval_cor_ls()
            if cmax_ < self.cmax:
                print("a = " + str(a))
                self.k = self.k_
                self.c = self.c_.copy()
                self.l_cor = copy.deepcopy(self.l_cor_)
                self.cmax = cmax_
                self.cor_ls()
            
            
    def eval_cor_ls(self):
        cmax = 0
        for i in self.e:
            if self.c_[i] > cmax:
                cmax = self.c_[i]
            for j in self.e[i]:
                if self.c_[i] == self.c_[j]:
                    return cmax, 0
        return cmax, 1    
        
    def min_color_ls(self, y):
        n = np.ones(self.k_)
        a = b = 0
        x = len(self.e[y])
        for i in self.e[y]:
            if self.c_[i] != -1 and n[self.c_[i]] != 0:
                n[self.c_[i]] = 0
                b += 1
            elif self.c_[i] == -1:
                a += 1
        if a == x:
            self.c_[y] = 0
        elif b == self.k_:
            self.k_ += 1
            self.c_[y] = self.k_ - 1
        else:
            for i in range(0, len(n)):
                if n[i] == 1:
                    self.c_[y] = i
                    break
    
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("\nError!")
        sys.exit(1)
  
    start = time.clock()
    v, l_adj = ler_instancia(str(sys.argv[1]))
    gc = grafo_cor(v,l_adj)
    
    end = time.clock()
    
    print("Num. de Cores = " + str(gc.k))
    for i in range(0,gc.k):
        print(str(i) + ":" + str(gc.l_cor[i]))
    
    print('Tempo = ' + "{0:.8f}".format(end - start) + " segundos")
    


    