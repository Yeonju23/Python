# 입출력
## 함수
> def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...

### 매개변수와 인수
- 매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수 
- 인수(arguments): 함수를 호출할 때 전달하는 입력값
> def add(a, b):  # a, b는 매개변수
    return a+b
print(add(3, 4))  # 3, 4는 인수

여러 개의 입력값을 받은 함수 만들기
> def add_many(*args): 
...     result = 0 
...     for i in args: 
...         result = result + i 
...     return result 
*args 처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 준다. 

[키워드 파라미터 kwargs]
매개변수 앞에 별 두개(**)를 붙이면 딕셔너리가 되고 모든 key=value 형태의 결과값이 그 딕셔너리에 저장된다. 

함수의 결과값은 언제나 하나!

특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 
함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 "함수만의 변수"

함수 안에서 함수 밖의 변수를 변경하는 방법
1. return 사용
> a = 1 
def vartest(a): 
    a = a +1 
    return a
a = vartest(a) 
print(a)

2. global 명령어 사용
> a = 1 
def vartest(): 
    global a 
    a = a+1
vartest() 
print(a)

=> 함수는 독립적으로 존재하는 것이 좋기 때문에 프로그래밍 시 global 명령어는 사용하지 않는 것이 좋다. 


lambda: 함수 생성할 때 사용하는 예약어, def 와 동일한 역할
- 보통 함수를 한줄로 간결하게 만들 때 사용
- def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에서 주로 사용
ex) add = lambda a,b: a+b
    result = add(3,4)

- lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다. 