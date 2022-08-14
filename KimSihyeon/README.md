### Rules
1. file name : 'mmdd_level_title.py'
2. source : Programmers
3. more details : [beniceto.tistory.com](https://beniceto.tistory.com)

### New insights
1. for문 대신 map() 함수를 적절히 이용해보기
2. N개의 최소공배수
```python
i = 1
while True :
    MAX = max(array)
    if all(MAX*i % a == 0 for a in array) :
        break
    else :
        i += 1
```
