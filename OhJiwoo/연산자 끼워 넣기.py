n=int(input())
data=list(map(int,input().split()))
a,s,m,d=map(int,input().split())
min_sum=1e9
max_sum=-1e9


def dfs(i,s):
  global a, s, m, d, min_sum, max_sum
  if i == n:
    min_sum=min(min_sum,s)
    max_sum=max(max_sum,s)
  else:
    if a >0 :
      a -= 1 
      dfs(i+1,s+data[i])
      a +=1
    if s >0 :
      s -=1
      dfs(i+1,s-data[i])
      s+=1
    if m>0 :
      m-=1
      dfs(i+1,s*data[i])
      m+=1
    if d>0 :
      d -=1
      dfs(i+1,int(s/data[i]))
      d+=1

dfs(1,data[0])
print(min_sum)
print(max_sum)
