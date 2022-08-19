### Rules
1. file name : 'mmdd_level_title.py'
2. source : Programmers
3. more details : [beniceto.tistory.com](https://beniceto.tistory.com)

### New insights
1. for문 대신 map() 함수를 적절히 이용해보기
2. N개의 최소공배수 : 2개의 최소공배수를 연속으로 구하는 방법 외에도 아래와 같은 방법이 있다.
```python
m = max(arr)
i = 1
while True :
      if all(m % a == 0 for a in arr) :
          break
      else :
          i += 1
          m = max(arr)*i
```
3. 124나라의 숫자 원리
![world124](./img/world124.jpg)
