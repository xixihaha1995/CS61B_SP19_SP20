while True:
    try:
        data = list(map(int, input().split()))
        print(sum(data[1:]))
    except Exception:
        break