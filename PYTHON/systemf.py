import sys

args = sys.argv[1:]
for i in args:
    filename = i
    f = open(filename, 'r', encoding='utf-8')
    data = f.read()
    f.close()
print(data)