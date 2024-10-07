# 필수 과제 가이드
## 숫자 맞추기 게임
### 1. 숫자 맞추기 게임 (필수)
```
 이 과제에서는 파이썬 프로그래밍 언어를 활용하여 숫자 맞추기 게임을 만드는 것이 목표입니다.
숫자 맞추기 게임은 컴퓨터가 생각한 숫자를 맞추는 게임으로, 플레이어는 숫자를 입력하고 컴퓨터가 생각한 숫자와 비교하여 “작다" 혹은 "크다" 힌트를 받아가며 숫자를 맞추는 게임입니다.
```
#### 과제  내용
1. 플레이어와 컴퓨터가 참여하는 숫자 맞추기 게임을 만드세요. 
2. 프로그램은 다음과 같은 기능을 포함해야 합니다.
- 컴퓨터는 1부터 10 사이의 랜덤한 숫자를 생성합니다. 
- 플레이어는 숫자를 입력하고, 입력한 숫자가 큰지 작은지 힌트를 얻습니다.
- 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.

#### 입출력 예시
→ 예시일 뿐 완전히 똑같이는 하지 않으셔도 돼요! 주어진 조건만 다 맞추시면 됩니다!
```
1과 10 사이의 숫자를 하나 정했습니다.
이 숫자는 무엇일까요?
예상 숫자: 5
너무 큽니다. 다시 입력하세요.
예상 숫자: 4
너무 큽니다. 다시 입력하세요.
예상 숫자: 3
정답입니다!
```

#### 참고 자료
- 랜덤 숫자 생성을 위한 random 모듈 사용법
```python
import random
```


## 클래스와 함수 사용하기
### 클래스와 함수 사용하기 (필수)
```
이 과제는 간단한 Python Class 활용 문제입니다.

처음 공부하시는 분들은 개념이나 활용 방법이 헷갈리실 수도 있으므로, 앞서 공부한 내용 복습 및 추가 학습을 하면서 진행해주세요. 
```

#### 과제 내용
- 이름, 성별, 나이를 입력받고, 이를 출력하는 프로그램을 작성해주세요.

#### 처리 조건
- 클래스 정의
    - `Person`이라는 이름의 클래스를 정의한다.
- 멤버 변수
    - `name`, `gender`, `age`라는 멤버 변수를 설정한다.
    - 각 변수는 객체가 생성될 때 초기화된다.
        - `name`: 이름을 저장하는 변수 (문자열)
        - `gender`: 성별을 저장하는 변수 (문자열, "male" 또는 "female")
        - `age`: 나이를 저장하는 변수 (정수형)
- 생성자
    - 생성자 `__init__`를 통해 객체 생성 시 이름, 성별, 나이를 초기화한다.
    - 매개변수로 이름(`name`), 성별(`gender`), 나이(`age`)를 받는다.
- 정보를 출력하는 함수 `display()`
    - `name`, `gender`, `age` 값을 출력하는 기능을 구현한다.
    - 이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력한다.
- 입력 및 출력
    - 사용자로부터 나이, 이름, 성별을 각각 입력받는다.
    - 입력된 값을 바탕으로 `Person` 객체를 생성하고, `display()` 함수를 통해 객체의 정보를 출력한다.

#### 예시 입출력
- 사용자 입력 예시
```
나이: 28
이름: 페이커
성별: male
```
​
```
출력 예시
이름: 페이커, 성별: male
나이: 28
```