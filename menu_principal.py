import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"


def jogar():    
    janela.destroy()
    import quiz

def sair():    
    janela.destroy()
    import login

def rank():    
    janela.destroy()
    import ranking
    
    

# Criar a janela principal
janela = tk.Tk()
janela.title("Menu Principal")
janela.geometry("1250x700+210+100")
janela.config(bg=background)
janela.resizable(width=False, height=False)

# Icone da janela
janela.iconbitmap("Imagens/logoprojetom.ico")

# Fundo da janela
frame=Frame(janela,bg="red")
frame.pack(fill="y")
imagem_fundo=PhotoImage(file="Imagens/menu.png")
Label(frame,image=imagem_fundo).pack()

# Botão Leaderboard
rank_img=PhotoImage(file="Imagens/rank.png")
largura = rank_img.width() // 3
altura = rank_img.height() // 2
rank_img = rank_img.subsample(3)  # Reduzir pela metade
botao_rank=Button(janela, image=rank_img, bg="white", bd=0, command=rank)
botao_rank.place(x=150, y=270)

# Botão JOGAR
jogar_img=PhotoImage(file="Imagens/jogar.png")
botao_jogar=Button(janela, image=jogar_img, bg="white", bd=0, command=jogar)
botao_jogar.place(x=527, y=368)

# botao Sair do jogo e voltar pra tela de login
sair_img=PhotoImage(file="Imagens/sair.png")
botao_sair=Button(janela, image=sair_img, bg="white", bd=0, command=sair)
botao_sair.place(x=962, y=290)


# Iniciar o loop principal da janela
janela.mainloop()
