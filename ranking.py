import tkinter as tk
from tkinter import PhotoImage

# Ler arquivo pontuacao.txt


def ler_pontuacoes():
    pontuacoes = []
    try:
        with open("G:\Meu Drive\Python\PI\pontuacao.txt", "r") as arquivo:
            for linha in arquivo:
                nome, pontuacao = linha.strip().rsplit(",", maxsplit=1)
                pontuacoes.append((nome, int(pontuacao)))
    except FileNotFoundError:
        print("Arquivo de pontuações não encontrado.")
    return pontuacoes


# Pontuações em ordem decrescente
def ordenar_pontuacoes(pontuacoes):
    pontuacoes.sort(key=lambda x: x[1], reverse=True)

def exibir_leaderboard():
    leaderboard = tk.Tk()
    leaderboard.title("Leaderboard")
    leaderboard.geometry("1250x700")
    leaderboard.resizable(width=False, height=False)

    # Icone da janela
    leaderboard.iconbitmap(r"G:\Meu Drive\Python\PI\Imagens\logoprojetom.ico")

    # Carregar a imagem de fundo
    imagem_fundo = PhotoImage(file=r"G:\Meu Drive\Python\PI\Imagens\ranking.png")

    # Criar um widget Label para exibir a imagem de fundo
    label_fundo = tk.Label(leaderboard, image=imagem_fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    pontuacoes = ler_pontuacoes()
    ordenar_pontuacoes(pontuacoes)
    
    # nome_label = tk.Label(leaderboard)
    # nome_label.grid(row=0, column=0, padx=10, pady=60, bd=0, sticky='ew')
    
    pontuacao_label = tk.Label(leaderboard, bg="#cddff6")
    pontuacao_label.grid(row=0, column=1, padx=10, pady=60, sticky='ew')
    


    

    for i, pontuacao in enumerate(pontuacoes[:10]):
        user_frame = tk.Frame(leaderboard, relief="solid", borderwidth=1, bg="#cddff6")
        user_frame.grid(row=i+1, column=0, padx=(100, 0), pady=(10, 0), ipady=(1), sticky='nsew')

        colocacao_label = tk.Label(user_frame, text=f"{i+1}º", bg="#cddff6", font=("Arial", 16), anchor="w")
        colocacao_label.pack(side=tk.LEFT, padx=5, pady=1)

        nome_label = tk.Label(user_frame, text=pontuacao[0], bg="#cddff6", font=("Arial", 16))
        nome_label.pack(side=tk.LEFT, padx=5, pady=1)

        user_frame2 = tk.Frame(leaderboard, relief="solid", borderwidth=1, bg="#cddff6")
        user_frame2.grid(row=i+1, column=1, padx=(0, 40), pady=(10, 0), ipadx=(150), sticky='nsew')

        pontuacao_label = tk.Label(user_frame2, text=str(pontuacao[1]), bg="#cddff6", font=("Arial Bold", 16))
        pontuacao_label.pack(padx=1, pady=1)

    # Configurar linhas
    for i in range(len(pontuacoes) + 1):
        leaderboard.grid_rowconfigure(i, weight=0)

    # Centralizar 
    leaderboard.grid_columnconfigure(0, weight=1)
    leaderboard.grid_columnconfigure(1, weight=0)


    # botao Sair do rank e voltar pro menu
    def sair():    
        leaderboard.destroy()
        import menu_principal

    sair_img=PhotoImage(file=r"G:\Meu Drive\Python\PI\Imagens\voltar2.png")
    botao_sair=tk.Button(leaderboard, image=sair_img, bg="#cddff6", bd=0, command=sair)
    botao_sair.place(x=45, y=45)


    leaderboard.mainloop()
    




exibir_leaderboard()
