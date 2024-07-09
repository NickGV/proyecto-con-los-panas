import tkinter as tk
import random
from tkinter import ttk

def pc_play():
  pc_play = random.randint(1,3)
  return pc_play


def eval_play(p_option):
  pc_option = pc_play()
  if p_option == 1:
    print("1")
  elif p_option == 2:
    print("2")
  elif p_option == 3:
    print("3")
  elif p_option == 4:
    return
  else :
    print("ganamos")


def main(root):
  root.config(width=300, height=200)
  root.title("piedra papel o tijera ")

  boton = ttk.Button(text="piedra",width=20, command=lambda: eval_play(1))
  boton.place(x=400, y=550)

  boton = ttk.Button(text="papel",width=20, command=lambda: eval_play(2))
  boton.place(x=600, y=550)

  boton = ttk.Button(text="tijera",width=20, command=lambda: eval_play(3))
  boton.place(x=800, y=550)

 # boton = ttk.Button(text="SALIR")

root = tk.Tk()
main(root)
root.mainloop()



  
