while True:
    try:
        t = int(input())
        for _ in range(t):
            data = list(map(str, input().split()))
            data.sort()
            print(data)
    except Exception:
        break