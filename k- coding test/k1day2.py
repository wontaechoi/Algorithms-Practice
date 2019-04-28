# Python 3


from itertools import product
import random
from random import *


def frievald(a, b, c, r_list):
    global k, n
    r_list=[]
    if k == 1:
        r_list= [[1]]
    else:
        for q in range(5):
            r= [0] * k
            for i in range(0, k) : 
                r[i] = (int)(random()*2) % 2
            
            r_list.append(r)
        
    for r in r_list:
        br = [0] * k
        
        
        for i in range(k) : 
            for j in range(k) : 
                br[i] = br[i] + b[i][j] * r[j] 
      
        cr = [0] * k
        for i in range(k) : 
            for j in range(k) : 
                cr[i] = cr[i] + c[i][j] * r[j] 
      
        axbr = [0] * k
        for i in range(k) : 
            for j in range(k) : 
                axbr[i] = axbr[i] + a[i][j] * br[j] 
      
        for i in range(k) : 
            if (axbr[i] - cr[i] != 0) : 
                return False
                  
    return True    



test_case = int(input())
for t in range(test_case):
    n,m,k = map(int,input().split())
    x = []
    for i in range(k):
        row = list(map(int, input().split()))
        x.append(row)
    y = []
    for i in range(k):
        row = list(map(int, input().split()))
        y.append(row)    
        
    R= []
    for i in range(n):
        row = list(map(int, input().split()))
        R.append(row)
    
    
    
    block_matrix = []
    for i in range(n - k+1):
        for j in range(m - k+1):
            temp = []
            for z in range(k):
                t = R[i+z][j:k+j]
                temp.append(t)
            block_matrix.append(temp)
            
    count = 0
    
    #r_list = list(product(range(2), repeat=k))
    
    for b_m in block_matrix:
        s_found = frievald(x,b_m,y, [])
        if s_found == True:
            count +=1
    print(count)
