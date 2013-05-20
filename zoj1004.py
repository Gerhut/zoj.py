def get_iolist(in_list, out_str, out_list = [], stack = []):
    if len(out_list) == len(out_str):
        yield []
        return
        
    if in_list:
        stack.append(in_list.pop())
        for iolist in get_iolist(in_list, out_str):
            yield ['i'] + iolist
        in_list.append(stack.pop())
    if stack and out_str[len(out_list)] == stack[-1]:
        out_list.append(stack.pop())
        for iolist in get_iolist(in_list, out_str):
            yield ['o'] + iolist
        stack.append(out_list.pop())

try:
    while True:
        in_list = list(raw_input().strip())[::-1]
        out_str = raw_input().strip()
        print '['
        for iolist in get_iolist(in_list, out_str):
            print ' '.join(iolist), ''
        print ']'
except EOFError:
    pass
