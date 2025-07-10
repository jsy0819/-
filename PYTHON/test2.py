a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#shirt 안 들어감 O

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

a = range(1,101)
for i in a:
    print(i, end=" ")

print()

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)

result = [n for n in numbers if n % 2 == 1]
print(result)

# 1부터 10까지 정수에서 3의 배수를 리스트 형태로 출력하세요.

numbers = range(1,11)
result = []
for i in numbers:
    if i % 3 == 0:
        result.append(i)
print(result)

# 1부터 10까지 정수에서 5의 배수에 5의 배수가 아닌 값을 더하여
# 리스트 형태로 출력하세요.

numbers = range(1,11)
result5 = []
summod = 0
for i in numbers:
    if i % 5 == 0:
        result5.append(i)
    else:
        summod += i
result = []
for k in result5:
    result.append(k+summod)
print(summod)
print(result5)
print(result)

print('-'*50)

# 1부터 100까지 중 2의 배수이고 3의 배수인 수를 리스트 형태로 구하세요.

numbers = range(1,101)
result23 = []
for i in numbers:
    if i % 2 == 0 and i % 3 == 0:
        result23.append(i)
print(result23)

result23 = [i for i in range(1,101) if i % 2 == 0 and i % 3 == 0]
print(result23)