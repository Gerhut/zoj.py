def s(p):
    s = []
    n = 0
    for i in p:
        s.extend(['('] * (i - n) + [')'])
        n = i
    return ''.join(s)


def w(s):
    p = []
    w = []
    for i, v in enumerate(s):
        if v == '(':
            p.append(i)
        else:
            q = p.pop()
            c = 0
            for sv in s[q:i]:
                if sv == '(':
                    c += 1
            w.append(str(c))
    return w

if __name__ == '__main__':
    for i in xrange(input()):
        input()
        print ' '.join(w(s(map(int, raw_input().split()))))
