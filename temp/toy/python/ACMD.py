while True:
    data = list(map(int, input().split()))
    if data[0] == 0: break
    print(sum(data[1:]))