import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

isused=[0]*n
arr2=[]

def nm7(k):
    if k==m:
        print(*arr2)
        return
    for i in range(n):
        arr2.append(arr[i])
        nm7(k+1)
        arr2.pop()

nm7(0)