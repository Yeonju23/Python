# 파일 생성하기
> 파일 객체 = open(파일 이름, 파일 열기 모드)

f = open("새파일.txt", 'w')
f.close()

파일열기모드	설명
r	읽기모드 - 파일을 읽기만 할 때 사용
w	쓰기모드 - 파일에 내용을 쓸 때 사용
a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

- 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성된다. 

[파일 경로와 슬래시(/)]
- 파일 경로 표시 시 슬래시(/)사용
- 역슬래시(\)를 사용한다면 \\를 사용하거나 r"C:\doit\새파일.txt"와 같이 문자열 앞에 r(raw string)를 덧붙여 사용해야 한다. 

[파일을 스기 모드로 열어 출력값 적기]: 파일 객체 f의 write 함수를 사용!!
> f = open("C:/doit/새파일.txt", 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()


[프로그램의 외부에 저장된 파일을 읽는 여러가지 방법]
1. readline 함수 이용하기
> line = f.readline()
    print(line)
    f.close()

모든 줄을 읽고 싶을 때 
> while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()

파일을 열고 닫는 것을 동시에 처리하고 싶다면 with문 사용

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

파이썬에선 sys 모듈을 사용하여 매개 변수를 직접 줄 수 있다. 
