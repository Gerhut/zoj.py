def valid(eid):
    if board[eid] == 'X':
        return False
        
    for prev in board[eid / size * size : eid : 1][::-1]:
        if prev == 'O':
            return False
        elif prev == 'X':
            break
        
    for prev in board[eid % size : eid : size][::-1]:
        if prev == 'O':
            return False
        elif prev == 'X':
            break

    return True

def work(eid = 0):
    if eid == size * size:
        return 0
    after_count = work(eid + 1)
    if valid(eid):
        board[eid] = 'O'
        after_count = max(after_count, work(eid + 1) + 1)
        board[eid] = '.'
        
    return after_count

while True:
    size = int(raw_input())
    if size == 0:
        break
    board = []
    for n in range(size):
        board.extend(list(raw_input()))
    print work()
