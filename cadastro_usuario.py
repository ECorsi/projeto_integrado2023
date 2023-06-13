import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

def cadastrar():
    username = usuario.get()
    password = senha.get()
    admincode = acesso_admin.get()
    name = nome_usuario.get()
    register = ra_usuario.get()

    if admincode=="1234":

        if(username=="" or username=="Usuário") or (password=="" or password=="Senha"):
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            try:
                conexao = mysql.connector.connect(host="localhost",user="root",password="ritdiw-jomjiw-8jIxbe")
                cursor = conexao.cursor()
            except:
                messagebox.showerror("Conexão","Falha na conexao com o banco de dados") 
            
            try:
                command= "create database Registro_usuario"
                cursor.execute(command)

                command= "use database Registro_usuario"
                cursor.execute(command)

                command= """ CREATE TABLE login (
                        IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
                        Usuario VARCHAR(100) NOT NULL UNIQUE,
                        Senha VARCHAR(100),
                        RA VARCHAR(15) NOT NULL UNIQUE,
                        Nome VARCHAR(40) NOT NULL,
                        Pontuacao INT DEFAULT 0
                            )
                            """
                cursor.execute(command)


            except:
                cursor.execute("use Registro_usuario")
                conexao = mysql.connector.connect(host="localhost",user="root",password="ritdiw-jomjiw-8jIxbe",database="Registro_usuario")
                cursor = conexao.cursor()
                command="insert into login (Usuario, Senha, Nome, RA) values (%s,%s,%s,%s)"
                cursor.execute(command,(username, password, name, register))
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Cadastrado", "Cadastro realizado com sucesso!")
            
            

    else:
        messagebox.showerror("Código de Acesso", "Digite o código de Administrador correto")


def login():
    janela.destroy()
    import login

# Criar a janela principal
janela = tk.Tk()
janela.title("Janela de Login")
janela.geometry("1250x700+210+100")
janela.config(bg=background)
janela.resizable(width=False, height=False)

# Icone da janela
janela.iconbitmap("Imagens/icone.ico")

# Fundo da janela
frame=Frame(janela,bg="red")
frame.pack(fill="y")
imagem_fundo=PhotoImage(file="Imagens/cadastro.png")
Label(frame,image=imagem_fundo).pack()

acesso_admin= Entry(frame, width=17, fg="red", border="0", font=("Arial Bold", 20), show="*")
acesso_admin.focus()
acesso_admin.place(x=525, y=110)

# Usuário
def usuario_entrar(e):
    usuario.delete(0, "end")
    
def usuario_sair(e):
    nome=usuario.get()
    if nome=="":
        usuario.insert(0, "Usuário")

usuario=Entry(frame, width=18, fg="grey", bg="white", border=0, font=("Arial Bold", 20))
usuario.insert(0, "Usuário")
usuario.bind("<FocusIn>", usuario_entrar)
usuario.bind("<FocusOut>", usuario_sair)
usuario.place(x=220, y=270)

# Nome do aluno
def nomeusuario_entrar(e):
    nome_usuario.delete(0, "end")
    
def nomeusuario_sair(e):
    nome=nome_usuario.get()
    if nome=="":
        nome_usuario.insert(0, "Nome")

nome_usuario=Entry(frame, width=18, fg="grey", bg="white", border=0, font=("Arial Bold", 20))
nome_usuario.insert(0, "Nome")
nome_usuario.bind("<FocusIn>", nomeusuario_entrar)
nome_usuario.bind("<FocusOut>", nomeusuario_sair)
nome_usuario.place(x=825, y=270)

# RA do aluno
def rausuario_entrar(e):
    ra_usuario.delete(0, "end")
    
def rausuario_sair(e):
    nome=ra_usuario.get()
    if nome=="":
        ra_usuario.insert(0, "RA")

ra_usuario=Entry(frame, width=18, fg="grey", bg="white", border=0, font=("Arial Bold", 20))
ra_usuario.insert(0, "RA")
ra_usuario.bind("<FocusIn>", rausuario_entrar)
ra_usuario.bind("<FocusOut>", rausuario_sair)
ra_usuario.place(x=825, y=400)

# Senha
def senha_entrar(e):
    senha.delete(0, "end")

def senha_sair(e):
    if senha.get()=="":
        senha.insert(0, "Senha")

senha = Entry(frame,width=15,fg="grey", border=0,bg="white", font=("Arial Bold", 20), show="*")
senha.insert(0, "Senha")
senha.bind("<FocusIn>", senha_entrar)
senha.bind("<FocusOut>", senha_sair)
senha.place(x=220,y=400)

# Mostrar/Esconder Senha 

def esconder():
    global button_mode

    if button_mode:
        botao_olho.config(image=esconder_senha, activebackground="white")
        senha.config(show="*")
        button_mode= False
        
    else:
        botao_olho.config(image=mostrar_senha, activebackground="white")
        senha.config(show="")
        button_mode= True


button_mode=True
esconder_senha=PhotoImage(file="Imagens/esconder.png")
mostrar_senha=PhotoImage(file="Imagens/mostrar.png")
botao_olho=Button(frame, image=esconder_senha, bg="#fff", bd=0, command=esconder)
botao_olho.place(x=450,y=405)

# Botão CADASTRAR
cadastrar_img=PhotoImage(file="Imagens/bcadastrar2.png")
botao_cadastrar=Button(janela, image=cadastrar_img, bg="#cddff6", bd=0, command=cadastrar)
# botao_cadastrar=Button(janela,text="CADASTRAR", bg="#4b74bc", fg="white",width=12, height=1, font=("Microsoft YaHei UI Light", 18), bd=0, command=cadastrar)
botao_cadastrar.place(x=460, y=510)

#Botao voltar p/ tela de login

voltar_img=PhotoImage(file="Imagens/voltar.png")
botao_voltar=Button(janela, image=voltar_img, bg="#cddff6", bd=0, command=login)
botao_voltar.place(x=45, y=45)

# Iniciar o loop principal da janela
janela.mainloop()
