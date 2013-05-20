import sys

def possible_ballons(score, min_ballon = 2):
    if score == 1:
        yield set()
    else:
        for ballon in xrange(min_ballon, min(101, score + 1), 1):
            if score % ballon == 0:
                for sub_ballons in possible_ballons(score / ballon, ballon + 1):
                    yield set([ballon]) | sub_ballons

def work(more, less):
    more_ballons_list = list(possible_ballons(more))
    less_ballons_list = list(possible_ballons(less))
    
    if len(less_ballons_list) == 0:
        return more

    if len(more_ballons_list) == 0:
        return less
    
    for more_ballons in more_ballons_list:
        for less_ballons in less_ballons_list:
            if len(more_ballons & less_ballons) == 0:
                return more
    return less

for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    more, less = map(int, line.split(' '))
    if more < less:
        more, less = less, more
    print work(more, less)
