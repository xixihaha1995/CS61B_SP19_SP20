while True:
    try:
        drop = int(input())
        data = list(map(str, input().split()))
        print('$'.join(sorted(data)))
    except Exception:
        break