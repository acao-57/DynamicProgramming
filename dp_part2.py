import sys

def R(n, s, c, r):
    table = [[0]*(s + 1) for _ in range(n + 1)] #table[n+1][s+1]

    #base
    for i in range(n + 1):
        table[i][0] = 0
    for j in range(1, s + 1):
        table[0][j] = sys.maxsize

    for i in range(1, n + 1): #policies
        for j in range(1, s + 1): #savings

            if (j < c[i - 1]): 
                option1 = r[i - 1]
            else:
                option1 = table[i-1][j-c[i-1]] + r[i - 1]

            option2 = table[i-1][j]
            table[i][j] = min(option1, option2)

    print(table[n][s])

if __name__ == "__main__":
    n,s = map(int,input().split())
    c = list(map(int,input().split()))
    r = list(map(int, input().split()))


    if s > sum(c):
        print(-1)
    else:
        R(n, s, c, r)