#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

n = int(input())

word = []

for i in range(n):
    word.append(input())

#set을 사용해 중복 제거
set_word = list(set(word))

sort_word = []

# append()리스트의 마지막에 인자로 전달된 아이템을 추가
for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)