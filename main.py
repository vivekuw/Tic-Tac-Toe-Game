import tkinter

def check_winner():
    global turns,game_over
    turns+=1
        # horizontal
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            label.config(text=board[row][0]["text"]+' is the winner',foreground=COLOR_YELLOW)
            for column in range(3):
                board[row][column].config(foreground=COLOR_YELLOW,background=BACKGROUND_COLOR)
            game_over=True
            return
        # vertically
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
            label.config(text=board[0][column]["text"] + ' is the winner', foreground=COLOR_YELLOW)
            for row in range(3):
                board[row][column].config(foreground=COLOR_YELLOW,background=BACKGROUND_COLOR)
            game_over=True
            return
        # DIAGONALLY
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        label.config(text=board[0][0]["text"] + ' is the winner', foreground=COLOR_YELLOW)
        for i in range(3):
            board[i][i].config(foreground=COLOR_YELLOW, background=BACKGROUND_COLOR)
        game_over = True
        return

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        label.config(text=board[0][2]["text"] + ' is the winner', foreground=COLOR_YELLOW)
        board[0][2].config(foreground=COLOR_YELLOW, background=BACKGROUND_COLOR)
        board[1][1].config(foreground=COLOR_YELLOW, background=BACKGROUND_COLOR)
        board[2][0].config(foreground=COLOR_YELLOW, background=BACKGROUND_COLOR)
        game_over = True
        return

    if turns==9:
        game_over=True
        label.config(text='Tie!',foreground=COLOR_YELLOW, background=BACKGROUND_COLOR)

def set_tile(row,column):
    global current_player
    if board[row][column]["text"]!="":
        return

    board[row][column]["text"] = current_player

    if current_player==playerO:
        current_player=playerX
        board[row][column]['foreground'] = COLOR_BLUE
    else:
        current_player=playerO

    label["text"]=current_player+"'s turn"
    check_winner()

def new_game():
    global turns,game_over
    turns=0
    game_over=False

    label["text"]=current_player+"'s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=COLOR_BLUE,background=BACKGROUND_COLOR)

COLOR_RED = '#F52B21'
COLOR_BLUE= '#4928F5'
BACKGROUND_COLOR='#343434'
COLOR_YELLOW='#FFDE57'

playerX='X'
playerO='O'
current_player=playerX
turns=0
game_over=False
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

window=tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=f"{current_player}'s turn", font=('Consolas',20),
                      background=BACKGROUND_COLOR,foreground='white')
label.grid(row=0,column=0,columnspan=3,sticky="we") # "we means the label is stretching west to east"


for row in range(3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame, text='',font=('Consolas',50,"bold"),
                                          background=BACKGROUND_COLOR,foreground=COLOR_RED,
                                          width=4,height=1,
                                          command=lambda row=row,column=column:set_tile(row,column))
        board[row][column].grid(row=row+1,column=column)

button=tkinter.Button(frame,text="restart",font=('Consolas',20),
                      background=BACKGROUND_COLOR,foreground='white',
                      command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}") # format of w*h + x+y
window.mainloop()