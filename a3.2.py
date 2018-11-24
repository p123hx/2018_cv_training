def show(board):
    print(f'{board[1]}{board[2]}{board[3]}')
    print(f'{board[4]}{board[5]}{board[6]}')
    print(f'{board[7]}{board[8]}{board[9]}')    
    
def win(board,winconbinations):
    for a,b,c in winconbinations:
        if board[a+1] == board[b+1] == board[c+1]:
            print('Winner:',board[a+1])
            return True
    if sum((pos=='X' or pos=='O') for pos in board)==9:
        print('Winner: None')
        return True
def tic():
    board=[None]+list(range(9))
    winconbinations=[
        
       (0, 1, 2),
       (3, 4, 5),
       (6, 7, 8),
       (0, 3, 6),
       (1, 4, 7),
       (2, 5, 8),
       (0, 4, 8),
       (2, 4, 6),
    ]
    show(board)
    d={
        '(0,0)':1,
        '(0,1)':2,
        '(0,2)':3,
        '(1,0)':4,
        '(1,1)':5,
        '(1,2)':6,
        '(2,0)':7,
        '(2,1)':8,
        '(2,2)':9
    }
    t=input().split('->')
    step=0
    for player in 'XO'*9:
        index=t[step]
        n=d[index]
        print(player,'-->',n-1)
        
        board[n]=player
        show(board)
        step+=1
        if win(board,winconbinations):
            return
        
tic()
        
