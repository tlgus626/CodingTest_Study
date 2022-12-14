### Rules
1. file name : 'mmdd_level_title.py'
2. source : Programmers or Baekjoon
3. more details : [beniceto.tistory.com](https://beniceto.tistory.com)

### New insights
1. for문 대신 `map()` 함수를 적절히 이용해보기
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
3. . 가장 큰 수 : 모든 원소가 `0`이 아닌 이상 ''.
```python
def solution(numbers):
    v = sorted(list(map(str,numbers)),key=lambda x: x*3,reverse=True)    
    return ''.join(v) if not all(c == "0" for c in v) else "0"
    # str(int()) 랑 비교했을 때 소요시간이 더 짧음.
    # return str(int(''.join(v)))
```
4. defaultDict() : value를 따로 지정하지 않아도 `0`으로 채워줌
5. divmod()
```python
divmod(x,y) == (x//y, x%y)
```
6. 이진 변환 반복하기 - 재귀 함수 ver.
```python
def solution(s):
    def convert(s, z, r):
        # 0제거 후 길이
        ch = bin(s.count("1"))[2:]
        # z: 회전 수, r: 0 제거 개수 
        return [z,r+s.count("0")] if ch == s else convert(ch, z+1, r+s.count("0"))
    return convert(s, 0, 0)
```
