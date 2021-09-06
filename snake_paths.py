def move(board,snake,action):
    '''
    If an action is valid, it performs it, if not, it returns invalid.

    We only have to check that the new position of the head is valid,
    since the rest of the cells become positions that were previously valid
    
    '''
    if action=='L':
        new_head=[snake[0][0]-1,snake[0][1]]
        if snake[0][0]==0 or new_head in snake[:-1]:
            return "invalid"
    
    elif action=='R':
        new_head=[snake[0][0]+1,snake[0][1]]
        if snake[0][0]==board[0]-1 or new_head in snake[:-1]:
            return "invalid"
    
    elif action== 'U':
        new_head=[snake[0][0], snake[0][1]-1]
        if snake[0][1]==0 or new_head in snake[:-1]:
            return "invalid"
    
    else:#action == D
        new_head=[snake[0][0], snake[0][1]+1]
        if snake[0][1]==board[1]-1 or new_head in snake[:-1]:
            return "invalid"    
    

    #valid
    new_snake=[new_head]
    for i in range(len(snake)-1):
        new_snake.append(snake[i])
    return new_snake


def numberOfAvailableDifferentPaths(board,snake,depth):
    '''
    BFS is used until we reach the given depth. 
    
    We are saving the states of the current depth to obtain those of the next depth
    
    '''
    actions=['L','R','U','D']
    current_depth=0
    states=[snake]
    new_states=[]
    while current_depth<depth:
        if len(states)==0:
            break
        for state in states:
            for action in actions:
                movement= move(board,state,action)
                if movement !='invalid':
                    new_states.append(movement)
        states=new_states
        new_states=[]
        current_depth+=1
    return len(states)%(1_000_000_007)

if __name__ == '__main__':
    board1 = [4,3]
    snake1 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth1 = 3

    board2 = [2,3]
    snake2 = [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
    depth2 = 10

    board3 = [10,10]
    snake3 = [[5,5], [5,4], [4,4], [4,5]]
    depth3 = 4




    assert(numberOfAvailableDifferentPaths(board1,snake1,depth1)==7)
    assert(numberOfAvailableDifferentPaths(board2,snake2,depth2)==1)
    assert(numberOfAvailableDifferentPaths(board3,snake3,depth3)==81)
    print("Tests passed successfully")
        
        