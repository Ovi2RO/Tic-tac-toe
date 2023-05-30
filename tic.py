from tkinter import *
import sv_ttk
import time

def evaluate_board():
    if check_winner() == players[0]:
        return -1
    elif check_winner() == players[1]:
        return 1
    elif empty_spaces() is False:
        return 0
    return 0

def minimax(depth, maximizing_player):
    if check_winner() != False or depth == 0:
        return evaluate_board()

    if maximizing_player:
        maxEval = -float('inf')
        for row in range(3):
            for column in range(3):
                if buttons[row][column]["text"] == "":
                    buttons[row][column]["text"] = players[1]
                    evaluation = minimax(depth - 1, False)
                    buttons[row][column]["text"] = ""
                    maxEval = max(maxEval, evaluation)
        return maxEval
    else:
        minEval = float('inf')
        for row in range(3):
            for column in range(3):
                if buttons[row][column]["text"] == "":
                    buttons[row][column]["text"] = players[0]
                    evaluation = minimax(depth - 1, True)
                    buttons[row][column]["text"] = ""
                    minEval = min(minEval, evaluation)
        return minEval

def computer_move():
    global player
    bestScore = -float('inf')
    bestMove = None
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                buttons[row][column]["text"] = players[1]
                score = minimax(0, False)
                buttons[row][column]["text"] = ""
                if score > bestScore:
                    bestScore = score
                    bestMove = (row, column)

    buttons[bestMove[0]][bestMove[1]]["text"] = players[1]
    if check_winner() is False:
        player = players[0]
        label.config(text=(players[0] + " turn"))
    elif check_winner() is True:
        label.config(text=(players[1] + " wins"))
    elif check_winner() == "Tie":
        label.config(text=("Tie!!!"))

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
                computer_move()
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!!!"))

# def computer_move():
#     global player
#     bestScore = -float('inf')
#     bestMove = None

#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]["text"] == "":
#                 buttons[row][column]["text"] = players[1]
#                 score = minimax(0, False)
#                 buttons[row][column]["text"] = ""
#                 if score is not None and score > bestScore:
#                     bestScore = score
#                     bestMove = (row, column)

#     buttons[bestMove[0]][bestMove[1]]["text"] = players[1]
#     if check_winner() is False:
#         player = players[0]
#         label.config(text=(players[0] + " turn"))
#     elif check_winner() is True:
#         label.config(text=(players[1] + " wins"))
#     elif check_winner() == "Tie":
#         label.config(text=("Tie!!!"))

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = players[0]
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#1C1C1C")
    if check_winner() == False:
        computer_move()



window = Tk()
window.title("Tic-Tac-Bully")


sv_ttk.set_theme("dark")

players = ["X", "O"]
player = players[0]
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
label = Label(window, text=player + " turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(window, text="Restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()