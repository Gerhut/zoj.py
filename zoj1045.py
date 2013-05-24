import bisect


def result(length, results=[0, 1.0 / 2], results_length=[2]):
    max_length = results[results_length[0] - 1]
    while max_length < length:
        max_length += 1.0 / (results_length[0] + 1)
        results_length[0] += 1
        results.append(max_length)
        index = results_length[0] - 1
    else:
        index = bisect.bisect(results, length)
    return index

if __name__ == '__main__':
    while True:
        length = input()
        if length == 0:
            break
        print '%d card(s)' % (result(length))
