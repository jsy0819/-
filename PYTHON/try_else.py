try:
    age = int(input("나이를 입력하세요."))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age<=18:
        print("가라")
    else:
        print("ok 콜!")