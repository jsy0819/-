'''treeHit = 0
while treeHit < 10:
    treeHit +=1
    print(f"나무를 {treeHit}만큼 찍었습니다.")
    if treeHit==10:
        print(f"나무가 넘어갑니다.")'''

coffee = 10
while True:
    money = int(input("돈을 넣어주세요"))
    if money == 300:
        print("coffee")
        coffee -= 1
    elif money > 300:
        print(" send mod")
        coffee -= 1
    else:
        print("돈이 부족합니다.")
    if coffee == 0:
        print("coffee out")
        break