'''
def is_add(number):
    return '홀수입니다.'
def is_add(number):
    return '짝수입니다.'

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

input1 = int(input('첫번째 숫자를 입력하세요.'))
input2 = int(input('두번째 숫자를 입력하세요.'))
total = int(input1)+int(input2)
total = int(input1+input2)
'''
print("you" "need" "love")
print("you", "need", "love")

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

# 1단계: 파일에 쓰기
f = open('text1.txt', 'w', encoding='utf-8')
f.write("Life is too short\nyou need java")
f.close()

# 2단계: 파일을 읽기 모드로 다시 열기
f = open('text1.txt', 'r', encoding='utf-8')
body = f.read()
f.close()

# 3단계: 문자열 수정 및 새 파일에 저장
body = body.replace("java", "python")

f = open('test.txt', 'w', encoding='utf-8')
f.write(body)
f.close()

import sys

args = sys.argv[1:]
result = 0
for i in args:
    result += int(i)

print(result)