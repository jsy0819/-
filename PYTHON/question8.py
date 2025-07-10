import random

locations = ["마법의 숲", "고대 성", "용의 동굴", "신비의 사막"]
treasures = ["마법 지팡이", "황금 왕관", "보석 목걸이"]
enemies = ["늑대", "해적", "드래곤"]

#print(int(random.random()*100))
findAni = 30
attackSuc = 40
findRadio = 50
upRadio = 20
getTreasure = []

while True:
    UserStatus = input("\n탐험, 상태, 종료 중 하나를 입력하세요. ").strip()
    #print(UserStatus)
    NowLocation = random.choice(locations)
    if UserStatus == '종료':
        print("게임을 종료합니다.")
        break
    elif UserStatus == '상태':
        print(getTreasure)
        print(NowLocation)
    elif UserStatus == '탐험':
        MeetRadio = int(random.random()*100)
        if MeetRadio > findAni:
            anim = random.choice(enemies)
            UserAttckYN = input(f"{anim}을 만났습니다. 도망치기, 공격 중 하나를 입력하세요. ").strip()
            if UserAttckYN == '공격':
                AttackRadio = int(random.random()*100)
                if AttackRadio > attackSuc:
                    print("공격에 성공하였습니다.")
                    findRadio += upRadio
                else:
                    print("당신은 사망하였습니다.")
                    break
            else:
                print("당신은 도망치는데 성공하였습니다.")

        fR = int(random.random()*100)
        gT = random.choice(treasures)
        if fR >= findRadio and treasures:
            getTreasure.append(gT)
            treasures.remove(gT)
            messageAppend = f"{gT}를 획득하였습니다."
        else:
            messageAppend = ""
        print(getTreasure)
        print(f"당신은 {NowLocation}에 도착하였습니다. {messageAppend}")

    if len(getTreasure) == 3:
        print("당신은 모든 아이템을 획득하였습니다.")
        break












'''
import random

locations = ["마법의 숲", "고대 성", "용의 동굴", "신비의 사막"]
treasures = ["마법 지팡이", "황금 왕관", "보석 목걸이"]
enemies = ["늑대", "해적", "드래곤"]
getTreasure = []

print("\n🌟 마법의 세계에 오신 것을 환영합니다! 보물을 모두 찾으면 승리합니다.")

while True:
    print("\n1. 탐험하기")
    print("2. 상태 확인하기")
    print("3. 게임 종료하기")
    choice = input("\n원하는 행동을 선택하세요 (1~3): ").strip()

    if choice == "1":
        location = random.choice(locations)
        print(f"\n🗺️ {location}에 도착했습니다.")

        # 적 등장
        if random.randint(0, 100) < 40:
            enemy = random.choice(enemies)
            print(f"⚔️ 갑자기 {enemy}이(가) 나타났습니다!")
            action = input("👉 어떻게 할까요? (공격 / 도망): ").strip()
            if action == "공격":
                if random.randint(0, 100) < 60:
                    print("🎯 공격 성공! 적을 물리쳤습니다.")
                else:
                    print("💀 공격 실패... 당신은 사망하였습니다.")
                    break
            else:
                print("🏃‍♂️ 재빠르게 도망쳤습니다!")

        # 보물 획득
        if treasures and random.randint(0, 100) < 60:
            treasure = random.choice(treasures)
            treasures.remove(treasure)
            getTreasure.append(treasure)
            print(f"✨ {location}에서 '{treasure}'를 발견했습니다!")
        else:
            print("🔍 이 장소에서는 특별한 것을 찾지 못했습니다.")

    elif choice == "2":
        print(f"\n📦 보유 중인 보물: {', '.join(getTreasure) if getTreasure else '없음'}")
        print(f"📍 현재 위치 중 일부: {', '.join(random.sample(locations, 2))}")

    elif choice == "3":
        print("\n🛑 게임을 종료합니다. 다음에 또 만나요!")
        break

    else:
        print("⚠️ 잘못된 입력입니다. 1, 2, 3 중 하나를 골라주세요.")

    # 게임 종료 조건
    if len(getTreasure) == 3:
        print(f"\n🏆 모든 보물을 수집하였습니다! 당신의 승리입니다!")
        break
'''