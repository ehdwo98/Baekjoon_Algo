import sys
input=sys.stdin.readline

n=int(input())
arr=list(int(input()) for _ in range(n))

arr.sort()
for a in arr:
   print(a)