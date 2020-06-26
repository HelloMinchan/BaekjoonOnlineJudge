import sys
input = sys.stdin.readline


def DFS(n):
    # 기저 사례
    if memoization[n]:
        return memoization[n]

    # 기저 사례
    if n < 2:
        return n

    memoization[n] = DFS(n - 1) + DFS(n - 2)

    return memoization[n]


N = int(input())

memoization = [0] * (N + 1)

print(DFS(N))
