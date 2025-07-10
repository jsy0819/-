# 규칙 :
# 컴퓨터가 랜덤으로 "동물" 또는 "동물이 아닌 것"(예: 책, 나무)을 제시.
# 사용자가 "예"(동물) 또는 "아니오"(동물이 아님)로 맞추기.
# 맞추면 점수 1점, 틀리면 힌트 제공 후 재도전 기회.
# 3문제 완료 시 점수로 결과 출력(90점 만점 기준).
# 한번도 안 틀리면 보너스 점수 10점.
# 한번이라도 틀리면 보너스 점수 0점.

#items = ["고양이", "강아지", "책", "나무", "펭귄", "자동차"]

import random

items = ["고양이", "강아지", "책", "나무", "펭귄", "자동차"]
animals = ["고양이", "강아지", "펭귄"]

Score = 0
CorrectCount = 0
InputCount = 0
TotalCount = 3

while InputCount < TotalCount:
    item = random.choice(items)
    items.remove(item)

    answer = input(f"{item}은/는 동물인가요? y/n ").lower().strip()
    InputCount += 1

    if answer == "y":
        if item in animals:
            CorrectCount += 1
            Score += 30
            print("정답입니다!")
        else:
            print("틀렸습니다!")
else:
    if item not in animals:
        CorrectCount += 1
        Score += 30
        print("정답입니다!")
    else:
        print("틀렸습니다!")

if CorrectCount == 3:
    Score += 10
    print(f"모든 문제를 맞추셨습니다! 보너스 점수 10점을 받아서 최종 점수는 {Score}입니다.")
elif InputCount==3:
    print(f"최종 점수는 {Score}입니다.")