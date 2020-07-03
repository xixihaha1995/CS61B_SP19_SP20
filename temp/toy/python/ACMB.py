def add(a, b):
    return a+b

line = int(input())

for i in range(line):
    line = input().split()
    print(add(int(line[0]), int(line[1])))