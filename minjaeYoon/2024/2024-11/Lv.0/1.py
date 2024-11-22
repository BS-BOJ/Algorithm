# 1. [PCCE] 기출문제 1번 문자 출력
message = "Let's go!"

print("3 \n2 \n1")
print(message)

# 2. 코딩 기초 트레이닝 문자열 출력하기
str = input()
print(str)

# 3. 코딩 기초 트레이닝 a와 b 출력하기
a, b = map(int, input().strip().split(' '))
print(f'a = {a}')
print(f'b = {b}')

# 4. 코딩 기초 트레이닝 문자열 반복해서 출력하기
str, n = input().strip().split(' ')
n = int(n)
print(n*str)

# 5. 코딩 기초 트레이닝 대소문자 바꿔 출력
str = input()

sentence = []
for i in str:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    sentence.append(i)

print(''.join(sentence))

# 6. 코딩 기초 트레이닝 특수문자 출력 -> 구글링

# 'r' 사용하기 : \가 많이 사용되는 케이스는 r
print(r'!@#$%^&*(\'"<>?:;')

# \ ' " 앞에 붙이기
print('!@#$%^&*(\\\'"<>?:;')

# 7. 코딩 기초 트레이닝 덧셈식 출력
a, b = map(int, input().strip().split(' '))
c = a + b
print(f'{a} + {b} = {c}')

# 8. 코딩 기초 트레이닝 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')

sentence = str1 + str2

print(''.join(sentence))

# 9. 코딩 기초 트레이닝 문자열 돌리기

# 내 풀이
str = input()

for i in str:
    print(i)

# 감탄한 풀이
print('\n'.join(input()))

# 10. 코딩 기초 트레이닝 홀짝
a = int(input())

if a%2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 11. 코딩 기초 트레이닝 문자열 겹쳐쓰기

# 내 풀이
def solution(my_string, overwrite_string, s):
    answer = ''
    sentence = my_string[:s], overwrite_string, my_string[s+len(overwrite_string):]
    return answer.join(sentence)

my_string, overwrite_string, s = input().strip().split(' ')
s = int(s)

print(solution(my_string, overwrite_string, s))

# -> 없어도 그만 + 제일 많이 본 답변도 같은 구조

# 12. 코딩 기초 트레이닝 문자열 섞기

# 내 풀이
def solution(str1, str2):
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return (''.join(answer))

print(solution('aaaaa', 'bbbbb'))

# 타인 풀이
def solution(str1, str2):
    answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return answer

# 13. 코딩 기초 트레이닝 문자 리스트를 문자열로 표현하기
def solution(arr):
    answer = ''.join([arr[i] for i in range(len(arr))])
    return answer

# 14. 코딩 기초 트레이닝 문자열 곱하기
def solution(my_string, k):
    answer = ''.join([my_string for i in range(k)])
    return answer

# 15. 코딩 기초 트레이닝 더 크게 합치기

def solution(a, b):
    answer = 0
    answer1 = '' + str(a) + str(b)
    answer2 = '' + str(b) + str(a)
    if int(answer1) > int(answer2):
        answer += int(answer1)
    else:
        answer += int(answer2)
    return answer

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


# 16. 코딩 기초 트레이닝 두 수 연산값 비교
