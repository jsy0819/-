# 행운의 숫자 맞추기 게임
# 규칙:
# 컴퓨터가 1부터 50까지의 랜덤 숫자를 생성.
# 사용자가 숫자를 입력해 추측.
# "춥다" (멀었음), "따뜻하다" (가까움) 힌트 제공.
# 컴퓨터가 생각하는 숫자와 5보다 더 벌어지면 춥다. 
# 컴퓨터가 생각하는 숫자와 2안에 있으면 엄청 따뜻하다.

# 남은 시도 횟수도 보여주기
# 그 외는 따뜻하다.
# 7번 이내에 맞추면 성공, 초과 시 게임 종료.

# import random
# random.randint(1,50)

import random
ComputersNumber = random.randint(1,50)
#print(ComputersNumber)
InputCount = 0
TotalCount = 7

while TotalCount > InputCount :
    # print(TotalCount)
    # print(InputCount)
    try:
        UserInput = int(input("숫자를 입력하세요."))
        InputCount += 1
        ComUserDiff = abs(ComputersNumber - UserInput)
        if ComUserDiff>5:
            print("춥다")
        elif ComUserDiff >2:
            print("따뜻하다")
        elif ComUserDiff ==0:
            print("정답")
            break
        else :
            print("엄청 따뜻하다")
    except ValueError as e:
        print("정확한 숫자를 입력하세요.")

if ComputersNumber==UserInput:
    print(f"정답은 {ComputersNumber}이고 당신은 {InputCount}번만에 맞추셨습니다.")

# Lotto = random.sample(range(1,46),6)
# Lotto.sort()
# print(Lotto)