import random

r_number = random.randint(1,50)
tries = 0

while True:
    try:
        random50 = int(input("1 ~ 50 랜덤 숫자 맞추기 : "))
        tries += 1

        if tries > 7:
            print("7번 이내에 정답을 맞추지 못하여 실패")
            break

        if abs(random50 - r_number) == 0:
            print("정답")
            break
        elif abs(random50 - r_number) <= 2:
            print("따뜻하다")
        elif abs(random50 - r_number) <= 5:
            print("춥다")
        else:
            print("너무 춥다")

    except ValueError:
        print("숫자만 입력")

print("정답은", r_number)