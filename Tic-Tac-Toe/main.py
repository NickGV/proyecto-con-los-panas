# Modulos
import tkinter as tk
from tkinter import messagebox

board = [["", "", ""], ["", "", ""], ["", "", ""]]

player = "x"
buttons = []


def win():
    global player, board
    print(player)
    for row in board:
        if row[0] == row[1] == row[2] == player:
            print("row")
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            print("col")
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        print("diag")
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        print("")
        return True
    return False


def reset_board():
    global board, player
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = "x"

    for btn in buttons:
        btn.config(text="", state="normal")


def click(x, y, btn):
    global player, board
    board[x][y] = player
    btn.config(text=f"{player}")
    btn["state"] = "disabled"
    if win():
        messagebox.showinfo("Ganador!", f"{player} gana!")
        reset_board()
    else:
        if player == "x":
            player = "o"
        else:
            player = "x"


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x320")

frame1 = tk.Frame(root)
frame1.grid(column=0, row=1, padx=10)

frame2 = tk.Frame(root)
frame2.grid(column=0, row=2, padx=10)

frame3 = tk.Frame(root)
frame3.grid(column=0, row=3, padx=10)

button1 = tk.Button(
    frame1,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(0, 0, button1),
)
button1.grid(row=1, column=1)
buttons.append(button1)

button2 = tk.Button(
    frame1,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(0, 1, button2),
)
button2.grid(
    row=1,
    column=2,
)
buttons.append(button2)

button3 = tk.Button(
    frame1,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(0, 2, button3),
)
button3.grid(row=1, column=3)
buttons.append(button3)
# frame2
button4 = tk.Button(
    frame2,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(1, 0, button4),
)
button4.grid(row=2, column=1)
buttons.append(button4)
button5 = tk.Button(
    frame2,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(1, 1, button5),
)
button5.grid(row=2, column=2)
buttons.append(button5)
# frame3

button6 = tk.Button(
    frame2,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(1, 2, button6),
)
button6.grid(row=2, column=3)
buttons.append(button6)

button7 = tk.Button(
    frame3,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(2, 0, button7),
)
button7.grid(row=3, column=1)
buttons.append(button7)

button8 = tk.Button(
    frame3,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(2, 1, button8),
)
button8.grid(row=3, column=2)
buttons.append(button8)

button9 = tk.Button(
    frame3,
    text="",
    font=("Arial", 20),
    width=5,
    height=2,
    command=lambda: click(2, 2, button9),
)
button9.grid(row=3, column=3)
buttons.append(button9)

root.mainloop()
