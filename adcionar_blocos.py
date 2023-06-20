import tkinter as tk


def add_button():
    root1 = tk.Tk()
    root1.title("Adicionar Bloco")

    
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

