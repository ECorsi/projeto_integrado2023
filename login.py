import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

# Função para realizar a verificação de login
def verificar_login():
    # Obtém as credenciais do usuário
    username = usuario.get()
    password = senha.get()
    

    try:
        # Conecta-se ao banco de dados MySQL
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ritdiw-jomjiw-8jIxbe",
            database="Registro_usuario")

        # Cria um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Executa a consulta para verificar o login
        query = "SELECT * FROM login WHERE Usuario = %s AND Senha = %s"
        cursor.execute(query, (username, password))

        # Verifica se há um resultado válido
        if cursor.fetchone():
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            
            janela.destroy()
            import menu_principal

             
            
            
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválido!")

        # Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()

    except mysql.connector.Error as erro:
        messagebox.showerror("Falha na conexao com o banco de dados", str(erro))

def cadastrar():
    janela.destroy()
    import cadastro_usuario

def regras():
    janela.destroy()
    import regras

# def recuperar():
#     janela.destroy()
#     import recuperar_senha


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
imagem_fundo=PhotoImage(file="Imagens/janela.png")
Label(frame,image=imagem_fundo).pack()

# Entrada do usuário
def usuario_entrar(e):
    usuario.delete(0, "end")
    
def usuario_sair(e):
    nome=usuario.get()
    if nome=="":
        usuario.insert(0, "Usuário")
        
usuario = Entry(frame,width=17,fg="grey", border=0,bg="white", font=("Arial Bold", 20))
usuario.insert(0, "Usuário")
usuario.bind("<FocusIn>", usuario_entrar)
usuario.bind("<FocusOut>", usuario_sair)
usuario.place(x=525,y=315)

# Senha do usuário
def senha_entrar(e):
    senha.delete(0, "end")

def senha_sair(e):
    if senha.get()=="":
        senha.insert(0, "Senha")

senha = Entry(frame,width=17,fg="grey", border=0,bg="white", font=("Arial Bold", 20), show="*")
senha.insert(0, "Senha")
senha.bind("<FocusIn>", senha_entrar)
senha.bind("<FocusOut>", senha_sair)
senha.place(x=525,y=400)

# Esconder/Mostrar Senha
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
botao_olho.place(x=750,y=405)


# Botao de Login
login_img=PhotoImage(file="Imagens/blogin.png")
botao_login=Button(janela, image=login_img, bg="#cddff6", bd=0, command=verificar_login)
# botao_login=Button(janela,text="LOGIN", bg="#4b74bc", fg="white",width=10, height=1, font=("arial italic", 16), bd=0, command=verificar_login)
botao_login.place(x=525, y=490)


# Botão Cadastrar-se
registrar_img=PhotoImage(file="Imagens/bcadastrar.png")
botao_cadastrar=Button(janela, image=registrar_img, bg="#cddff6", bd=0, command=cadastrar)
botao_cadastrar.place(x=558, y=550)

regras_img=PhotoImage(file="Imagens/bregras.png")
botao_regras=Button(janela, image=regras_img, bg="#0056e3", bd=0, command=regras)
botao_regras.place(x=958, y=550)

# Iniciar o loop principal da janela
janela.mainloop()
