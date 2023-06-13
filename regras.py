import tkinter as tk
from tkinter import *

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

# Criar a janela principal
regras = tk.Tk()
regras.title("Regras")
regras.geometry("1200x700")
regras.config(bg=background)
regras.resizable(width=False, height=False)


# Icone da janela
regras.iconbitmap("Imagens/logoprojetom.ico")

# Fundo da janela
frame=Frame(regras,bg="red")
frame.pack(fill="y")
imagem_fundo=PhotoImage(file="Imagens/regras.png")
Label(frame,image=imagem_fundo).pack()

def voltar():
    regras.destroy()
    import login



voltar_img=PhotoImage(file="Imagens/voltar.png")
botao_voltar=Button(regras, image=voltar_img, bg="#cddff6", bd=0, command=voltar)
botao_voltar.place(x=45, y=45)

regras.mainloop()
