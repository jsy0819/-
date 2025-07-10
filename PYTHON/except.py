print(type(Exception))

class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

'''
try:
    a = [1,2]
    4/0
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)



try:
    f = open("rkskekfk.txt", 'r')
except FileNotFoundError:
    pass
'''