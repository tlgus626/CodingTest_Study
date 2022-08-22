## 0822 스터디
#
### 1. 124 나라의 숫자 
#### 구현문제인듯
![programmers_level2_124-나라의-숫자_설명](https://user-images.githubusercontent.com/69744314/185778369-9fda40e7-7f38-4efe-b36b-3ac61b5d0706.jpg)

#
### 2. 가장 큰 수
#### 정렬
![programmers_level2_가장-큰-수_설명](https://user-images.githubusercontent.com/69744314/185778371-4ec0e0e3-e221-4fef-9306-eab6d30a135e.png)
#### 만들어진 리스트
![programmers_level2_가장-큰-수_참고](https://user-images.githubusercontent.com/69744314/185778372-17823d74-f433-469f-a3f5-e41a791acc48.png)

#
### 3. 뉴스 클러스터링
#### 구현
![programmers_level2_뉴스-클러스터링_설명](https://user-images.githubusercontent.com/69744314/185778373-5bdd8b6f-fce6-4a30-bf2f-6ead84b119d2.jpg)

#

### 0822 피드백
### 1. 124 나라의 숫자
#### divmod(n-1, 3): n-1을 3으로 나눈 몫과 나머지를 한번에 구해주는 함수
#### 재귀로 계속 몫을 나눠줌

###

### 2. 가장 큰 수
#### sort를 시킬 때 key로 각 숫자를 문자형으로 전환하고 * 3 해서 같은 자릿수만 비교하는 방식이 가능
#### 숫자형을 string으로 바꿔서 비교하는 것이 아스키 코드를 쓰는거였음

###

### 3. 뉴스 클러스터링
#### 중복원소를 그대로 넣은 리스트를 만들고, 중복원소 개수를 카운팅하면서 교집합 개수를 세고, 중복원수 개수를 빼줌
#### zip()을 쓸 때, 안에 넣은 리스트 앞에 *를 붙이면, 거꾸로 뭔가 됨?
#### defaultdict() 함수 안에 int를 쓰면, value를 전부 0으로 채워줌
#### 딕셔너리의 value 값이 해당 키(반복되는 답)의 개수
