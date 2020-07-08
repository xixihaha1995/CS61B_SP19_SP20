def add(a, b):
    return a+b


t = int(input())
for i in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    print(add(a, b))