import queue
def dfs(v):
    global mat,chk1,n
    print(v,end=" ")
    chk1[v]=1
    for i in range(1,n+1):
        if mat[v][i] and not chk1[i]:
            dfs(i)
def bfs(v):
    global mat,chk2,n
    q=queue.Queue()
    q.put(v)
    chk2[v]=1
    while q.qsize():
        x=q.get()
        print(x,end=" ")
        for i in range(1,n+1):
            if mat[x][i] and not chk2[i]:
                q.put(i)
                chk2[i]=1
n,m,v=map(int,input().split())
mat=[[0]*(n+1) for _ in range(n+1)]
chk1,chk2=[0 for _ in range(n+1)],[0 for _ in range(n+1)]
while m:
    a,b=map(int,input().split())
    mat[a][b]=mat[b][a]=1
    m-=1
dfs(v)
print()
bfs(v)
print()