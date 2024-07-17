import tkinter as tk 
from tkinter import ttk 


def main(root):
  root.config(width=300, height=200)
  root.title("piedra papel o tijera ")

  boton = ttk.Button(text="piedra",width=20 command=lambda: eval_play(2))
  boton.place(x=400, y=550)

  boton = ttk.Button(text="papel",width=20, command=lambda: eval_play(2))
  boton.place(x=600, y=550)

  boton = ttk.Button(text="tijera",width=20 command=lambda: eval_play(2))
  boton.place(x=800, y=550)

 # boton = ttk.Button(text="SALIR")

root = tk.Tk()
main(root)
root.mainloop()