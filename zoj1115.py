while True:
    n = input()
    if n == 0:
        break
    s = n % 9
    print s if s > 0 else 9
