d = "_abcdefghijklmnopqrstuvwxyz."
while True:
    line = raw_input().strip()
    if line == '0':
        break
    k, c = line.split(' ')
    k = int(k)
    n = len(c)
    p = [' '] * n
    for i, cl in enumerate(c):
        p[k * i % n] = d[(d.find(cl) + i) % 28]
    print ''.join(p)
