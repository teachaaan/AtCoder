import sys
def getInt(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


def reverse(i):
    strList = list(str(i))
    return int("".join(strList[::-1]))


def minimize(i):
    fx = i
    while True:
        if reverse(fx) < fx:
            fx = reverse(fx)
        else:
            return fx


N, K = LI()
if minimize(K) != K:
    print(0)
else:
    Kr = reverse(K)
    numSet = set()
    while True:
        if K <= N:
            numSet.add(K)
            K = 10 * K
        else:
            break

    while True:
        if Kr <= N:
            numSet.add(Kr)
            Kr = 10 * Kr
        else:
            break
    print(len(numSet))
