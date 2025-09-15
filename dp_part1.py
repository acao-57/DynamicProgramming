MOD = (10**9) + 7

import sys

def R(n,s, c, r): #naive recursion solution
    #return min(R(n-2, s-c[n-1], r, c) + r[n-1], R(n-2, s, r, c))
    #enact policy i: encir ri risk and must achieve savings of j - ci
    #from first i-1 policies

    #do not enact policy i: still need to achieve j savings from first i-1 policies

    #after eval both, pick smaller one

    #impossible to achieve
    
    if s == 0:
        return 0
    elif n == 0:
        return sys.maxsize
    
    if (s >= c[n-1]):
        return min(R(n-1, s-c[n-1], c, r) + r[n-1], R(n-1, s, c, r))
    else: #(s < c[n-1]):
        return min(r[n-1], R(n-1,s, c, r))

if __name__ == "__main__":
    n,s = map(int,input().split())
    c = list(map(int,input().split()))
    r = list(map(int, input().split()))

    if s > sum(c):
        print(-1)
    else: 
        result = R(n, s, c, r)
        print(result)




    
