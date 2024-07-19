import tkinter as tk
import random

player_score = 3
pc_score = 3
choices = ["rock", "paper", "scissors"]

def pc_play():
    return random.choice(choices)

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
    check_game_over()

def updateOptions(p_option, pc_option):
    label_pc_option.configure(text=f"{pc_option}")
    label_player_option.configure(text=f"{p_option}")

def update(result):
    global pc_score, player_score

    if result == "lose":
        pc_score += 1
        player_score -= 1
        label_result.config(text="You lose", fg="red")
    elif result == "draw":
        label_result.config(text="Draw")
    else:
        player_score += 1
        pc_score -= 1
        label_result.config(text="You Won", fg="green")

    label_score_pc.config(text=f"Computer: {pc_score}")
    label_score_player.config(text=f"Me: {player_score}")

def check_game_over():
    if player_score == 0:
        label_result.config(text="Game Over: You lost!", fg="red")
        disable_buttons()
        boton_reset.grid(row=3, column=1, pady=10)
    elif pc_score == 0:
        label_result.config(text="Game Over: You won!", fg="green")
        disable_buttons()
        boton_reset.grid(row=3, column=1, pady=10)

def disable_buttons():
    boton_rock.config(state=tk.DISABLED)
    boton_paper.config(state=tk.DISABLED)
    boton_scissors.config(state=tk.DISABLED)

def reset_game():
    global player_score, pc_score
    player_score = 3
    pc_score = 3
    label_score_player.config(text=f"Me: {player_score}")
    label_score_pc.config(text=f"Computer: {pc_score}")
    label_result.config(text="")
    label_player_option.config(text="")
    label_pc_option.config(text="")
    enable_buttons()
    boton_reset.grid_forget()

def enable_buttons():
    boton_rock.config(state=tk.NORMAL)
    boton_paper.config(state=tk.NORMAL)
    boton_scissors.config(state=tk.NORMAL)

root = tk.Tk()
root.geometry("400x400")
root.title("Rock Paper Scissors")

label_score_player = tk.Label(root, text=f"Me: {player_score}", font=("Helvetica", 12))
label_score_player.grid(row=0, column=0, padx=20, pady=10)
label_score_pc = tk.Label(root, text=f"Computer: {pc_score}", font=("Helvetica", 12))
label_score_pc.grid(row=0, column=2, padx=20, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=1, column=1, pady=10)

label_player_option = tk.Label(root, text="", font=("Arial", 12))
label_player_option.grid(row=1, column=0, padx=20, pady=10)

label_pc_option = tk.Label(root, text="", font=("Arial", 12))
label_pc_option.grid(row=1, column=2)

boton_rock = tk.Button(root, text="rock", padx=8, pady=8, command=lambda: play("rock"))
boton_rock.grid(row=2, column=0)
boton_paper = tk.Button(root, text="paper", padx=8, pady=8, command=lambda: play("paper"))
boton_paper.grid(row=2, column=1)
boton_scissors = tk.Button(root, text="scissors", padx=8, pady=8, command=lambda: play("scissors"))
boton_scissors.grid(row=2, column=2)

boton_reset = tk.Button(root, text="Reset", padx=8, pady=8, command=reset_game)

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
