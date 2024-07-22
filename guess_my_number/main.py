#Modulos
import tkinter as tk
from tkinter import messagebox
#Funciones
min = 1
max = 100
current = (max - min) // 2

def lower():
    global min,max,current, label
    max = current - 1 
    current = (max + min) // 2
    label.config(text=f"Your number is: {current}")
  
    
def height():
  global min,max,current, label
  min = current + 1 
  current = (max + min) // 2
  label.config(text=f"Your number is: {current}")

def you_guessed():
    global current
    messagebox.showinfo("¡important message!","¡you guessed!")
    return 
def play():
  global label
  root.destroy()
  play = tk.Tk()
  play.title("Guess my number")
  play.geometry("300x300")
  
  label = tk.Label(text="Your number is: 50")
  label.grid(padx=10, pady=10)
  
  buttons = tk.Frame(play)
  buttons.grid(row=1,column=0, pady=10)
  
  lower_button = tk.Button(buttons, text="Lower", command=lower, padx=8, pady=8)
  lower_button.grid(row=1, column=0, )
  
  
  guessed_button = tk.Button(buttons, text="You guessed it", command=you_guessed, padx=8, pady=8)
  guessed_button.grid(row=1, column=1)
  
  
  height_button = tk.Button(buttons, text="Higher", command=height, padx=8, pady=8)
  height_button.grid(row=1, column=2)
  
  for i in range(2):
    play.grid_rowconfigure(i, weight=1)
  for j in range(1):
    play.grid_columnconfigure(j, weight=1)
  
  play.mainloop()
  
  
#Parte grafica

root = tk.Tk()
root.title("Guess my number")
root.geometry("300x300")

text_label = tk.Label(root, text="pick a number between 1 and 100")
text_label.pack(fill=tk.BOTH)

play_button = tk.Button(root, text="Play", command=play)
play_button.pack(fill=tk.BOTH)

#Inicio de aplicacion

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
for j in range(2):
    root.grid_columnconfigure(j, weight=1)
    
root.mainloop()
