from tkinter import *
import random
import sv_ttk

def score():
    if check_winner() is True:
        if player == "X":
            return -1
        else:
            return 1
    elif check_winner() == "Tie":
        return 0

# minimax function
def minimax(is_maximizing):
    if check_winner() is not False:
        return score()

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for column in range(3):
                if buttons[row][column]["text"] == "":
                    buttons[row][column]["text"] = "O"
                    score = minimax(False)
                    buttons[row][column]["text"] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for column in range(3):
                if buttons[row][column]["text"] == "":
                    buttons[row][column]["text"] = "X"
                    score = minimax(True)
                    buttons[row][column]["text"] = ""
                    best_score = min(score, best_score)
        return best_score

# computer move function
def computer_move():
    best_score = float('-inf')
    move = None

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                buttons[row][column]["text"] = "O"
                score = minimax(False)
                buttons[row][column]["text"] = ""
                if score > best_score:
                    best_score = score
                    move = (row, column)

    buttons[move[0]][move[1]]["text"] = "O"
def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
                computer_move()  # add this line to make the computer move after the player
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!!!"))


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
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
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
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#1C1C1C")


window = Tk()
window.title("Tic-Tac-Bully")

# Create the Tk instance before setting the theme
sv_ttk.set_theme("dark")

players = ["X", "O"]
player = random.choice(players)
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