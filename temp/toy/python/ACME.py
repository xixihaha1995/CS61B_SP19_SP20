while True:
    try:
        while True:
            t  = int(input())
            for _ in range(t):
                data = list(map(int, input().split()))
                print(sum(data[1:]))
    except Exception:
        break