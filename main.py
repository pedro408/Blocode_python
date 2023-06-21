import tkinter as tk
import adcionar_blocos as ab

#Cria uma função que ira forncer ao meu botão uma utilidade, neste caso essa função imprime quando eu clicko no botão
def button_click():
    print("Botão clicado!")

#Essa função sai do aplicativo
def sair():
    root.quit()


#Cria uma tela
root = tk.Tk()
root.title("Blocode")



#Cria uma label
label1 = tk.Label(root, text="Blocode")

#Cria botões se referindo a minha tela
button1 = tk.Button(root, text="Adicionar Bloco", command=ab.add_button)
button2 = tk.Button(root, text="Ver blocos", command=ab.ver_b)
button3 = tk.Button(root, text="Sair", command=sair)


#Faz a chamada dos meus botões

label1.pack()
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
