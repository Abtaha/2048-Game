import tkinter as tk
from gui import Game

import random
import operator


board = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [0, 2, 2, 0]
]


def addNum(board):
    a = random.randint(0,3)
    b = random.randint(0,3)
    
    if board[a][b] == 0:
        board[a][b] = 2
    else:
        a = []
        for x in range(4):
            for y in range(4):
                if board[x][y] != 0:
                    pass
                else:
                    a.append("a")
        
        if len(a) == 0:
            print("You lose")
            exit()
        
        addNum(board)

def logic(board, y, x, oper_n, alignment):
    if alignment == 0:
        oper = operator.add(y, oper_n)
        
        if oper >= 0 and oper <= 3:
            if board[oper][x] == 0:
                board[oper][x] = board[y][x]
                board[y][x] = 0
                
            elif board[oper][x] == board[y][x]:
                board[oper][x] = board[oper][x] + board[y][x]
                board[y][x] = 0
            
            logic(board, oper, x, oper_n, alignment)
            
    if alignment == 1:
        oper = operator.add(x, oper_n)
        
        if oper >= 0 and oper <= 3:
            if board[y][oper] == 0:
                board[y][oper] = board[y][x]
                board[y][x] = 0
            
            elif board[y][oper] == board[y][x]:
                board[y][oper] = board[y][oper] + board[y][x]
                board[y][x] = 0
                
            logic(board, y, oper, oper_n, alignment)
    
    
def changeBoard(press):
    if press == "Up":
        for y in range(4):
            for x in range(4):
                logic(board, y, x, -1, 0)
    
    elif press == "Down":
        for y in reversed(range(4)):
            for x in reversed(range(4)):
                logic(board, y, x, 1, 0)
    
    elif press == "Left":
        for y in range(4):
            for x in range(4):
                logic(board, y, x, -1, 1)
    
    elif press == "Right":
        for y in reversed(range(4)):
            for x in reversed(range(4)):
                logic(board, y, x, 1, 1)
                
    addNum(board)

def Pressed(e):
    press = e.keysym
    
    if press == "Up" or press == "Down" or press == "Right" or press == "Left":
        changeBoard(press)
    
    #addNum(board)
    app.draw(board)



root = tk.Tk()

root.title("2048")
root.geometry("500x500")

app = Game(master=root, colorCoded = True)


app.focus_set()
app.bind("<Key>", Pressed)


#addNum(board)
#addNum(board)

app.draw(board)

app.mainloop()