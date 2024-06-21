import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    name,kor,en,math=input().split()
    kor=int(kor)
    en=int(en)
    math=int(math)
    arr.append([name,kor,en,math])

arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for a in arr:
    print(a[0])