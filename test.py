def changeBoard(press):
    for x in range(4):
        for y in range(4):
            
            if press == "Up":
                operY = operator.sub(y, 1)
            elif press == "Down":
                operY = operator.add(y, 1)
            elif press == "Left":
                operX = operator.sub(x, 1)
            elif press == "Right":
                operX = operator.add(x, 1)
            
            if press == "Up" or press == "Down":
                if operY >= 0 and operY <= 3:
                    if board_n[x][y] == board_n[x][operY]:
                        board_n[x][operY] = board_n[x][y] + board_n[x][operY]
                        board_n[x][y] = 0
                    elif board_n[x][operY] == 0:
                        board_n[x][operY] = board_n[x][y]
                        board_n[x][y] = 0
                        
            elif press == "Left" or press == "Right":
                if operX >= 0 and operX <= 3:
                    if board_n[x][y] == board_n[operX][y]:
                        board_n[operX][y] = board_n[x][y] + board_n[operX][y]
                        board_n[x][y] = 0
                    elif board_n[operX][y] == 0:
                        board_n[operX][y] = board_n[x][y]
                        board_n[x][y] = 0