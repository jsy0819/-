total = 0
for a in range(1,1000):
    if a % 3 == 0 or a % 5 == 0:
        total += a
print(total)



import random

r_number = random.randint(1,100)
tries = 0

while True:
    try:
        me = int(input("숫자 맞추기 : "))
        tries += 1

        if me < r_number:
            print("Up")
        elif me > r_number:
            print("Down")
        else:
            print(f"{tries}번 시도해서 정답")
            break

    except ValueError:
        print("숫자만 입력")

print("정답은", r_number)