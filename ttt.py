theBoard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}
boardKeys =[]
for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')

    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn='X'
    count=0
    for i in range(10):
        printBoard(theBoard)
        print(f"It's turn of {turn} specify the place you want to go: ")
        move=input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+=1
        else:
            print("Sorry this cell is located. Choose another one.")

            continue

        if count >= 5:
            if ((theBoard['1']==theBoard['2']==theBoard['3']!=' ')or(theBoard['4']==theBoard['5']==theBoard['6']!=' ')or(theBoard['7']==theBoard['8']==theBoard['9']!=' ')or
            (theBoard['1']==theBoard['4']==theBoard['7']!=' ')or(theBoard['2']==theBoard['5']==theBoard['8']!=' ')or(theBoard['3']==theBoard['6']==theBoard['9']!=' ')or
            (theBoard['1']==theBoard['5']==theBoard['9']!=' ')or(theBoard['3']==theBoard['5']==theBoard['7']!=' ')):
                printBoard(theBoard)
                print("\nGane Over!!!\n")
                print(f"Player {turn} WON the game..")
                break

        if count == 9:
            print("\nGame Over!!!\n")
            print("The game is Tie!")
            break
        
        if turn == "X":
            turn="O"
        else:
            turn="X"

    restart = input("Do you want to restart? (y/n)")
    if restart =='y' or restart =='Y':
        for key in boardKeys:
            theBoard[key] = ' '
        game()

if __name__=="__main__":
    game()