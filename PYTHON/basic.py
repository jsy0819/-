'''money = True
if money:
    moveMethod = "택시타고 가라"
else:
    moveMethod = "걸어가라"
print(moveMethod)

x = 3
y = 2
if x>y:
    print("빙고")

money = 2000
taxiTax = 3000
if money >= taxiTax:
    Car = "택시타기"
elif money >= 1500:
    Car = "빨간 버스타기"
elif money >= 1000:
    Car = "지하철타기"
else:
    Car = "걸어가기"
print(Car)

money = 2000
taxiTax = 3000
if money > taxiTax:
    moveMethod = 'taxi'
elif money > taxiTax:
    moveMethod = 'thinking'
else:
    moveMethod = 'walkiing'
print(moveMethod)

money = 3000
taxiTax = 3000
if money > taxiTax:
    moveMethod = "택시타고 갈란다"
else:
    if money == taxiTax:
        moveMethod='고민한다'
    else:
        moveMethod = "걸어 갈란다"
print(moveMethod)'''

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시타고 가라')
elif card:
    print('택시타고 카드로 내려')
else:
    print('걸어가라')

score = 100
message = "success" if score >= 60 else "failure"
print(message)