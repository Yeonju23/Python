# Concatenation
import numbers


head = "Pyhton"
tail = " is Fun!"
text = head + tail

print(text)
print(text * 2)
print(len(text)) #문자열 길이 구하기

a = "Life is too short, You need Python"
print(a[3])
print(a[0:4])

b = "20010331Rainy"
date = b[:8]
weather = b[8:]
print(date)
print(weather)

# 문자열 포매팅
c1 = "I eat %d apples." % 3
print(c1)

c2 = "I eat %s apples." % "five"
print(c2)

number = 3
c3 = "I eat %d apples." % number
print(c3)

day = "three"
c4 = "I ate %d apples. so I was sick for %s days." % (number, day)
print(c4)

#정렬과 공백
print("%10s" % "hi")
print("%-10s" % "hi")
print("%0.5f" % 3.4156684)
print("%10.5f" % 3.4156684) #전체길이가 10개인 문자열 공간에서 소수점 다섯번째까지만 표시

#format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples".format(number))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

y = 3.42134234
print("{0:0.4f}".format(y))
print("{{ and }}".format())

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

