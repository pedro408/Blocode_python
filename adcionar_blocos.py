import tkinter as tk

#Neste Script, se encontra a função de adcionar blocos no botão de "Adicionar blocos"



memoria_dos_blocos = []


def add_button():
    root1 = tk.Tk()
    root1.title("Adicionar Bloco")

    #Nessa função ele cria uma tela e cria um botao com outra função que esta dentro de outra fução que cria outros blocos até por fim conseguir criar labels    
    def add_code():
        
        def add_bloco_inside():
        
        
            def adicionar_label():
                blocos = entry2.get()
                label = tk.Label(root2,text=blocos)
                print("adcionando label")
                label.pack()
                
                
                

            root2 = tk.Tk()
            root2.title("blocos")

            entry2 = tk.Entry(root2)
                    
                    
            
            button6 = tk.Button(root2,text = "adicionar ao seu code",command=adicionar_label)
                        
                    
            button6.pack()
            entry2.pack()
            
                

            


        nome_bloco = entry.get()  
        button5 = tk.Button (root1,text= nome_bloco,command=add_bloco_inside)

        

        button5.pack()
    
    entry = tk.Entry(root1)  # Create a text entry field
    entry.pack()

    
    

    button4 = tk.Button(root1, text = "inserir bloco", command = add_code)
    button4.pack()

    print("Botão clicado!")




def ver_b():
    root3 = tk.Tk()
    root3.title("Ver blocos")
    button7= tk.Button(root3,text="Pedro")
    memoria_dos_blocos.append(button7)
    button7.pack()
