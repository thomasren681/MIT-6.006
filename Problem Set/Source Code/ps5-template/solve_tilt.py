def solve_tilt(B, t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: M | List of moves that solves B (or None if B not solvable)
    '''
    M = []
    ##################
    # YOUR CODE HERE #
    ##################

    move_paths = {} # map a configuration to its moves from original B
    Transform = ('up', 'down', 'left', 'right')
    level = [] # records all different configurations ordered by number of moves from B
    level.append([B])
    transform = []
    move_paths[B] = tuple(transform)
    no_victory = not(victory(B,t))
    # Adj = build_adjacency(B)
    # level.append(Adj)
    while no_victory:
        level.append([])
        for u in level[-2]:
            for adj in build_adjacency(u):
                level[-1].append(adj)
            for i, b in enumerate(build_adjacency(u)):
                transform = list(move_paths[u])
                transform.append(Transform[i])
                if b not in move_paths:
                    move_paths[b] = tuple(transform)
                if victory(b, t):
                    M = move_paths[b]
                    no_victory = False

        # for b in level[-1]:
        #     if victory(b,t):
        #         M = move_paths[b]
        #         break


    return M

def victory(B,t):
    '''
    Input:  B | Starting board configuration
            t | Tuple t = (x, y) representing the target square
    Output: Bool value | True if a slider hit the target, False otherwise
    Done in O(1)-time
    '''
    if B[t[1]][t[0]] == 'o':
        return True
    else:
        return False

def build_adjacency(B):
    '''
    Input:  B | Starting board configuration
    Output: B_ | the four possible configuration after one tilt from B
    Done in O(1)-time
    '''
    B_ = []
    Transform = ('up','down','left','right')
    for transform in Transform:
        B_.append(move(B,transform))

    return B_

####################################
# USE BUT DO NOT MODIFY CODE BELOW #
####################################
def move(B, d):
    '''
    Input:  B  | Board configuration
            d  | Direction: either 'up', down', 'left', or 'right'
    Output: B_ | New configuration made by tilting B in direction d
    '''
    n = len(B)
    B_ = list(list(row) for row in B)
    if d == 'up':
        for x in range(n):  
            y_ = 0          
            for y in range(n):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ += 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'down':
        for x in range(n):  
            y_ = n - 1
            for y in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y_][x] == '.'):
                    B_[y][x], B_[y_][x] = B_[y_][x], B_[y][x]
                    y_ -= 1
                if (B_[y][x] != '.') or (B_[y_][x] != '.'):
                    y_ = y
    if d == 'left':
        for y in range(n):  
            x_ = 0          
            for x in range(n):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ += 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    if d == 'right':
        for y in range(n):  
            x_ = n - 1
            for x in range(n - 1, -1, -1):
                if (B_[y][x] == 'o') and (B_[y][x_] == '.'):
                    B_[y][x], B_[y][x_] = B_[y][x_], B_[y][x]
                    x_ -= 1
                if (B_[y][x] != '.') or (B_[y][x_] != '.'):
                    x_ = x
    B_ = tuple(tuple(row) for row in B_)
    return B_

def board_str(B):
    '''
    Input:  B | Board configuration
    Output: s | ASCII string representing configuration B
    '''
    n = len(B)
    rows = ['+' + (' - '*n) + '+']
    for row in B:
        rows.append(' |' + '  '.join(row) + '|')
    rows.append(rows[0])
    S = '\n'.join(rows)
    return S


if __name__=='__main__':
    B = (
                ('.', '.', '.', '.', '.', '.', '#'),
                ('.', '.', '.', '.', '.', '#', '.'),
                ('.', '.', '.', '.', '.', '#', '#'),
                ('.', '.', '.', '.', '.', '#', '#'),
                ('.', 'o', 'o', 'o', '.', '.', '.'),
                ('#', '#', '#', '.', '.', '.', '.'),
                ('#', '#', '#', 'o', '.', '.', '.'),
            )
    t = (4,3)
    print(board_str(B))
    M = solve_tilt(B,t)
    print(M)
