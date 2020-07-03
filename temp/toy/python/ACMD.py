while True:
    line = input().split()
    n = int(line[0])
    if n == 0:
        break
    sum = 0
    for i in range(n):
        sum += int(line[i+1])
    print(sum)