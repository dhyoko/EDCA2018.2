'''
@Diogo Hitoshi Yokoyama
Atividade 6 - EDCA -  16/10/18 - Mochila Inteira
'''
import numpy as np


def moc_solve(M,p,c):
    n = len(p)
    x = []
    
    g_m = np.zeros((2,M+1,n+1))
    for i in range(n-1, -1, -1):
        for y in range(0, M + 1):
            if p[i] <= y:
                if g_m[0][y][i+1] < g_m[0][y-p[i]][i+1] + c[i]:
                    g_m[0][y][i] = g_m[0][y-p[i]][i+1] + c[i]
                    g_m[1][y][i] = 1
            if g_m[1][y][i] == 0:
                g_m[0][y][i] = g_m[0][y][i+1]
    print(g_m)
    v = 0
    print("\nValor Maximo = " + str(g_m[0][M][0]))
    print("Item(s) usado(s) = ")
    for k in range(0, n):
        if g_m[1][M - v][k] == 1:
            x.append(1)
            v = v + p[k]
        else:
            x.append(0)
        print("x" + str(k + 1) + " = "  + str(x[k]))
                
            
if __name__ == "__main__":
    M = 5
    p = [4,3,2,1]
    c = [84,60,40,10]
    
    moc_solve(M,p,c)