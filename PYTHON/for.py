Alpa_number = ["one", "two", "three"]
for i in Alpa_number:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f'{number}번 학생은 합격')
    else:
        print(f'{number}번 학생은 불합격')

a = range(10)
print(a)
b = range(1,11)
print(b)
add = 0
for i in b:
    print(i)
add = add + i
print(add)