def dfs(i, now):
  global maxnum, minnum, p, s, m, d

  if i == N:
    maxnum = max(maxnum, now)
    minnum = min(minnum, now)

  else:
    if p > 0:
      p -= 1
      dfs(i+1, now + numlist[i])
      p += 1
    if m > 0:
      m -= 1
      dfs(i+1, now * numlist[i])
      m += 1
    if s > 0:
      s -= 1
      dfs(i+1, now - numlist[i])
      s += 1
    if d > 0:
      d -= 1
      dfs(i+1, int(now / numlist[i]))
      d += 1

dfs(1, numlist[0])

print(maxnum, "\n", minnum)
