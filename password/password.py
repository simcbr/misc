# https://code.google.com/codejam/contest/4214486/dashboard#s=p0

# the basic idea is to use the dynamic programming.
# 
# the question is to arrange k different keys in m positions. m>k
# 
# define function f(k,m) is the the number of combinations of assigning k different keys in m positions;
# it can be solved if we know the answer of a small size problem.
# 
# C(i,j) is selecting i elements from j elements.
# 
# f(k,m) = f(k-1,m-1)C(1,m) + f(k-1,m-2)C(2,m) + f(k-1,m-3)C(3,m) + ... + f(k-1,k-1)C(m-(k-1), m)

# where f(k-1,k-1)=(k-1)!


import sys
import scipy.misc as sc

fits={}

def assign(K,N):
    
    if K>N:
        print "error"
    
    if K in fits:
        if N in fits[K]:
            return fits[K][N]
    
    if K not in fits:
        fits[K]={}
        
    if K==1:
        fits[K][N]=1
    elif K==N:
        fits[K][N]=sc.factorial(N, exact=True)
    else:
        if K not in fits:
            fits[K]={}
        fits[K][N]=0
        for i in range(1,N-K+2):
            fits[K-1][N-i]=assign(K-1,N-i)
            fits[K][N] += fits[K-1][N-i]*sc.comb(N,i,exact=True)
        

    return fits[K][N]
        
        

def main(argv):
    
    inputfile = argv[0]
    fi = open(inputfile, "r")
    fo = open("passwordOutput.txt","w")
    line=fi.readline()
    casesNum = int(line)
    for i in range(casesNum):
        print i, "/", casesNum
        line=fi.readline()
        inputs=line.split()
        K=int(inputs[0])
        N=int(inputs[1]) 
        volumn = assign(K,N)
        volumn = volumn % (1000000007)
        fo.write("Case #" + str(i+1) + ": " + str(volumn) + "\n")
    fi.close()
    fo.close()

if __name__=="__main__":
    main(sys.argv[1:])