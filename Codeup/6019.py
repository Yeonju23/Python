'''
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

참고
y, m, d = input().split('.')
과 같이 변수들을 순서대로 나열하면 구분기호를 기준으로 잘라 순서대로 저장한다.

'''
y, m, d = input().split('.')

print(d,m,y,sep='-')
