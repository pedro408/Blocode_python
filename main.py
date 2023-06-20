import tkinter as tk
import adcionar_blocos as ab

def button_click():
    print("Botão clicado!")



root = tk.Tk()
root.title("Blocode")


label1 = tk.Label(root, text="Blocode")


button1 = tk.Button(root, text="Adicionar Bloco", command=ab.add_button)
button2 = tk.Button(root, text="Ver blocos", command=button_click)
button3 = tk.Button(root, text="Sair", command=button_click)



label1.pack()
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
