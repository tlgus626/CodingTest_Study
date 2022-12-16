n = int(input())
apt = []
for _ in range(n):
    temp = str(input())
    c = [int(s) for s in temp]
    apt.append(c)

def dfs(x, y):
    global cnt

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if apt[x][y] == 1:
        cnt += 1
        apt[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


# 함수 적용
result = 0
cnt_list = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) == True:
            result += 1
            cnt_list.append(cnt)

cnt_list = sorted(cnt_list)
print(result)
for i in cnt_list:
    print(i)