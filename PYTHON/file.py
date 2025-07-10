f = open("newfile.txt", 'w', encoding='utf-8')
for i in range(10):
    data = f"{i}번째 라인입니다.\n"
    f.write(data)
f.close()