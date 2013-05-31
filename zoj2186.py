for s in map(int, raw_input().split()):
    if s < 168:
        print 'CRASH %d' % (s,)
        break
else:
    print 'NO CRASH'
