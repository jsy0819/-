'''
a = range(2,10)
b = range(1,10)

for i in a:
    print(f"{i}단")
    for j in b:
        print(f"{i}*{j}={i*j}", end=" ")
    print("")
'''

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)