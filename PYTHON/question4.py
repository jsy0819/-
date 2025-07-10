import random

choices = ["가위", "바위", "보"]

while True:
    try:
        me = input("가위 바위 보(q 누르면 나가기) : ").strip()
        if me == 'q':
            break

        if me not in choices:
            raise ValueError("다시 내")
        
        com = random.choice(choices)
        print(f"컴퓨터 : {com}")
        
        if me == com:
            print("무승부")
        elif (
            me == "가위" and com == "보" or
            me == "바위" and com == "가위" or
            me == "보" and com == "바위"
        ):
            print("승리")
        else:
            print("패배")
        break
    except ValueError as e:
        print(e)