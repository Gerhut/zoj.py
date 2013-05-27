def calc_t9(key2letter):
    t9 = dict()
    for key, letters in key2letter.iteritems():
        for letter in letters:
            t9[letter] = key
    return t9

t9 = calc_t9({   '2': 'abc', '3': 'def',
    '4': 'ghi',  '5': 'jkl', '6': 'mno',
    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'})

for scenario in xrange(input()):
    print 'Scenario #%d:' % (scenario + 1)
    keys2word = dict()
    for i in xrange(input()):
        word, probability = raw_input().split()
        probability = int(probability)
        keys = []
        for index, letter in enumerate(word):
            keys.append(t9[letter])
            key_string = ''.join(keys)
            old_value = keys2word.get(key_string, (None, None))
            if probability > old_value[1] or \
                probability == old_value[1] and key_string < old_value[0]:
                keys2word[key_string] = (word[:index + 1], probability)
    for i in xrange(input()):
        keys = raw_input()
        for l in xrange(len(keys) - 1):
            print keys2word.get(keys[:l + 1], ('MANUALLY', None))[0]
        print
    print
