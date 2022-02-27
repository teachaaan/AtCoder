import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# 2/26 AC


N, M = LI()
A = LI()
B = LI()

for i in range(len(B)):
    if not B[i] in A:
        print('No')
        sys.exit()
    A[A.index(B[i])] = -1

print('Yes')
