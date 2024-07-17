import tkinter as tk
import random
from tkinter import ttk

player_score = 3
pc_score = 3
choices = ["rock", "paper", "scissors"]


def pc_play():
    pc_play = random.choice(choices)
    return pc_play


def play(p_option):
    pc_option = pc_play()
    updateOptions(p_option, pc_option)
    if p_option == "rock" and pc_option == "paper":
        update("lose")
    elif p_option == "paper" and pc_option == "scissors":
        update("lose")
    elif p_option == "scissors" and pc_option == "rock":
        update("lose")
    elif p_option == pc_option:
        update("draw")
    else:
        update("won")


def updateOptions(p_option, pc_option):
    label_pc_option.configure(text=f"{pc_option}")
    label_player_option.configure(text=f"{p_option}")


def update(result):
    global pc_score, player_score

    if result == "lose":
        pc_score += 1
        player_score -= 1
        label_result.config(text="You lose", fg="red")
        label_score_pc.config(text=f"Computer: {pc_score}")
        label_score_player.config(text=f"Me: {player_score}")
    elif result == "draw":
        label_result.config(text="Draw")
    else:
        player_score += 1
        pc_score -= 1
        label_result.config(text="You Won", fg="green")
        label_score_pc.config(text=f"Computer: {pc_score}")
        label_score_player.config(text=f"Me: {player_score}")


root = tk.Tk()
root.geometry("400x400")
root.title("rock paper or scissors ")


label_score_player = tk.Label(root, text=f"Me: 3", font=("Helvetica", 12))
label_score_player.grid(row=0, column=0, padx=20, pady=10)
label_score_pc = tk.Label(root, text=f"Computer: 3", font=("Helvetica", 12))
label_score_pc.grid(row=0, column=2, padx=20, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=1, column=1, pady=10)

label_player_option = tk.Label(root, text="", font=(" Arial", 12))
label_player_option.grid(row=1, column=0, padx=20, pady=10)

label_pc_option = tk.Label(root, text="", font=("Arial", 12))
label_pc_option.grid(row=1, column=2)

boton_rock = tk.Button(root, text="rock", padx=8, pady=8, command=lambda: play("rock"))
boton_rock.grid(row=2, column=0)
boton = tk.Button(root, text="paper", padx=8, pady=8, command=lambda: play("paper"))
boton.grid(row=2, column=1)
boton = tk.Button(
    root, text="scissors", padx=8, pady=8, command=lambda: play("scissors")
)
boton.grid(row=2, column=2)


for i in range(3):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)


root.mainloop()
