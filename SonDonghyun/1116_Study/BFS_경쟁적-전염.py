n, k = list(map(int, input().split()))

data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

s, x, y = list(map(int, input().split()))

from collections import deque

new_list = []
for i in range(n):
  for j in range(n):
    if data[i][j] != 0:
      new_list.append([data[i][j], i, j, 0])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


sort_k = sorted(new_list, key = lambda x: x[0])  

dq = deque(sort_k)
  
while dq:
    
  a = dq.popleft()
  
  if a[3] == s:
    break

  else:
    for i in range(4):
      nx = a[1] + dx[i]
      ny = a[2] + dy[i]

      if nx >= 0 and ny >= 0 and nx < n and ny < n:
        if data[nx][ny] == 0:
          data[nx][ny] = a[0]
          dq.append([a[0], nx, ny, a[3] + 1])

print(data[x - 1][y - 1])