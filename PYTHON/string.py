a = 80
b = 75
c = 55
print((a + b + c) / 3)

print("-" * 20)

print("홀수" if 13 % 2 else "짝수")

print("-" * 20)

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

print("-" * 20)

pin = "881120-1068234"
gender = "남자" if pin[7] in "13" else "여자"
print(f"{gender}입니다.")

print("-" * 20)

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

print("-" * 20)

a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

print("-" * 20)

a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

print("-" * 20)

a = (1, 2, 3)
a = a + (4,)
print(a)

print("-" * 20)

a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python'
print(a)
#a[[1]] = 'python'
#print(a)
a[250] = 'python'
print(a)

print("-" * 20)

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

print("-" * 20)

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

print("-" * 20)

