out_line = ''
try:
    while True:
        for word in raw_input().split():
            if len(word) == 0:
                continue
            elif word == '<br>':
                print out_line
                out_line = ''
            elif word == '<hr>':
                if len(out_line) > 0:
                    print out_line
                print '-' * 80
                out_line = ''
            else:
                if len(out_line) == 0:
                    out_line = word
                elif len(out_line) + 1 + len(word) <= 80:
                    out_line += ' ' + word
                else:
                    print out_line
                    out_line = word
except EOFError:
    if len(out_line) > 0:
        print out_line
