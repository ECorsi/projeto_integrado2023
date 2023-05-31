import tkinter as tk
from tkinter import messagebox

class Pergunta:
    def __init__(self, pergunta, options, resposta):
        self.pergunta = pergunta
        self.options = options
        self.resposta = resposta
    
    def display_pergunta(self):
        pergunta_label.config(text=self.pergunta, fg="black")
        for i, option in enumerate(self.options):
            option_botao[i].config(text=option, command=lambda i=i: game.check_resposta(i+1))

class Game:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.score = 0
        self.atual_pergunta = 0
        self.atual_timer = None
    
    def check_resposta(self, user_resposta):
        if self.atual_timer:
            root.after_cancel(self.atual_timer)
        
        pergunta = self.perguntas[self.atual_pergunta]
        if pergunta.resposta == user_resposta:
            self.score += 1
            self.mostrar_mensagem("Resposta correta!")
        else:
            self.mostrar_mensagem("Resposta incorreta!")
        
        self.atual_pergunta += 1
        if self.atual_pergunta < len(self.perguntas):
            self.limpa_mensagem()
            self.display_pergunta()
            self.start_timer()
        else:
            self.end_game()
    
    def display_pergunta(self):
        pergunta = self.perguntas[self.atual_pergunta]
        pergunta.display_pergunta()
    

    def end_game(self):
        final_score = self.score
        percentage = final_score / len(self.perguntas) * 100
        if final_score > 12:
            self.mostrar_mensagem(f"Parabéns! Você acertou {final_score} perguntas.\nPercentual de acerto: {percentage:.2f}%")
        else:
            self.mostrar_mensagem(f"Infelizmente você acertou apenas {final_score} perguntas. Tente novamente.\nPercentual de acerto: {percentage:.2f}%")
        save_score(user_name, final_score)    
    
    def mostrar_mensagem(self, mensagem):
        mensagem_label.config(text=mensagem)
    
    def limpa_mensagem(self):
        mensagem_label.config(text="")
    
    def start_timer(self):
        self.atualiza_timer(15)
    
    def atualiza_timer(self, restante):
        timer_label.config(text=f"Tempo restante: {restante}s")
        if restante <= 0:
            self.next_pergunta()
            return
        
        self.atual_timer = root.after(1000, self.atualiza_timer, restante - 1)
    
    def next_pergunta(self):
        self.atual_pergunta += 1
        if self.atual_pergunta < len(self.perguntas):
            self.limpa_mensagem()
            self.display_pergunta()
            self.start_timer()
        else:
            self.end_game()

def save_score(user_name, score):
    caminho = "G:\Meu Drive\Python\PI\pontuacao.txt"
    try:
        with open(caminho, "a") as arquivo:
            arquivo.write(f"{user_name},{score}\n")
    except IOError:
        print(f"Erro ao salvar a pontuação no arquivo {caminho}.")


def submit_name():
    global user_name
    user_name = name_entrada.get()
    if user_name.strip() == "":
        
        messagebox.showinfo("ERRO!", "Digite seu Nome!")
        name_entrada.delete(0, tk.END) 
        name_entrada.focus()  
        return
    name_frame.pack_forget()
    game_frame.pack()
    game.display_pergunta()
    game.start_timer()

#interface gráfica
root = tk.Tk()
root.title("QUIZ")
root.geometry("1250x700")
root.resizable(width=False, height=False)

#imagem de fundo
imagem = "G:\Meu Drive\Python\PI\Imagens\minigame.png"
background = tk.PhotoImage(file=imagem)


background_label = tk.Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#aba de por Nome
name_frame = tk.Frame(root, bg="#cddff6")
name_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  
name_frame.pack(expand=True, pady=50)


name_label = tk.Label(name_frame, text="Digite seu Nome e Sobrenome:", font=("Arial", 18), fg="#2C3E50", bg="#cddff6", bd=0)
name_label.pack(pady=10)

name_entrada = tk.Entry(name_frame, font=("Arial", 12))
name_entrada.pack(pady=10)

submit_botao = tk.Button(name_frame, text="Enviar", width=20, font=("Arial", 12), bg="#3498DB", fg="white", bd=0, command=submit_name)
submit_botao.pack(pady=10)


game_frame = tk.Frame(root, bg="#cddff6")

pergunta_label = tk.Label(game_frame, wraplength=600, font=("Arial", 14), fg="#2C3E50", bg="#cddff6", justify="left")
pergunta_label.pack(pady=150, expand=False, fill="both")

option_frame = tk.Frame(game_frame, bg="#cddff6", padx=50, pady=10) 
option_frame.pack(expand=True)

cores = ["#1ABC9C", "#3498DB", "#9B59B6", "#F1C40F"]
option_botao = []
for i in range(4):
    botao = tk.Button(option_frame, text=f"Opção {i+1}", width=20, font=("Arial", 12), bg=cores[i], fg="white", bd=0)
    option_botao.append(botao)

    option_botao[i].pack(side=tk.LEFT, padx=5, pady=5)

mensagem_label = tk.Label(game_frame, font=("Arial", 12), fg="black", bg="#cddff6")
mensagem_label.pack(pady=10)

timer_label = tk.Label(game_frame, font=("Arial", 12), fg="black", bg="#cddff6")
timer_label.pack(pady=10)

name_frame.pack()

#perguntas
pergunta1 = Pergunta("Qual é a estrutura de controle utilizada para executar um bloco de código repetidamente enquanto uma condição for verdadeira?", ["a) for loop", "b) if statement", "c) switch case", "d) while loop"], 4)
pergunta2 = Pergunta("Qual é a função utilizada para obter o tamanho de uma lista?", ["a) length()", "b) count()", "c) size()", "d) len()"], 4)
pergunta3 = Pergunta("Qual é o operador utilizado para realizar uma comparação de igualdade?", ["a) !=", "b) =", "c) ==", "d) >"], 3)
pergunta4 = Pergunta("Qual é a palavra-chave utilizada para definir uma função?", ["a) function", "b) def", "c) define", "d) fun"], 2)
pergunta5 = Pergunta("Qual é o método utilizado para adicionar um elemento ao final de uma lista?", ["a) append()", "b) add()", "c) insert()", "d) extend()"], 1)
pergunta6 = Pergunta("Qual é o operador utilizado para calcular o resto da divisão entre dois números?", ["a) %", "b) /", "c) //", "d) *"], 1)
pergunta7 = Pergunta("Qual é o método utilizado para remover um elemento de uma lista?", ["a) remove()", "b) delete()", "c) pop()", "d) discard()"], 3)
pergunta8 = Pergunta("Qual é a palavra-chave utilizada para interromper a execução de um loop?", ["a) stop", "b) exit", "c) break", "d) continue"], 3)
pergunta9 = Pergunta("Qual é a estrutura de controle utilizada para executar um bloco de código apenas se uma condição for verdadeira?", ["a) for loop", "b) if statement", "c) while loop", "d) switch case"], 2)
pergunta10 = Pergunta("Qual é o método utilizado para converter um número em uma string?", ["a) convert()", "b) num_to_str()", "c) format()", "d) str()"], 4)
pergunta11 = Pergunta("Qual é a função utilizada para ler a entrada do usuário?", ["a) read()", "b) get()", "c) input()", "d) scan()"], 3)
pergunta12 = Pergunta("Qual é a estrutura de controle utilizada para executar um bloco de código repetidamente com base em uma sequência?", ["a) for loop", "b) while loop", "c) if statement", "d) switch case"], 1)
pergunta13 = Pergunta("Qual é o método utilizado para ordenar uma lista em ordem crescente?", ["a) sorted()", "b) sort()", "c) order()", "d) arrange()"], 1)
pergunta14 = Pergunta("Qual é a estrutura de dados utilizada para armazenar um conjunto de elementos únicos?", ["a) list", "b) tuple", "c) dictionary", "d) set"], 4)
pergunta15 = Pergunta("Qual é o resultado da expressão booleana?\nTrue or False and not False", ["a) True", "b) False", "c) Indefinido", "d) Erro de sintaxe"], 1)
pergunta16 = Pergunta('O que será impresso na saída após a execução do seguinte código?\n\nx = 5\nif x > 10:\n        print("A")\nelif x > 5:\n       print("B")\nelse:\n     print("C")', ["a) A", "b) B", "c) C", "d) Nenhum valor será impresso"], 3)
pergunta17 = Pergunta("O que será impresso na saída após a execução do seguinte código?\n\nx = 3\nwhile x > 0:\n	  print(x)\n	x -= 1", ["a) 3 2 1", "b) 3 2", "c) 3", "d) Nenhum valor será impresso"], 1)
pergunta18 = Pergunta('O que será impresso na saída após a execução do seguinte código?\n\nfrutas = ["maçã", "banana", "uva"]\nfor index, fruta in enumerate(frutas):\n       print(index, fruta)', ["a) 1 maçã 2 banana 3 uva", "b) 0 maçã 1 banana 2 uva", "c) maçã banana uva", "d) 0 maçã, 1 banana, 2 uva"], 2)
pergunta19 = Pergunta("O que será impresso na saída após a execução do seguinte código?\n\nnumeros = [1, 2, 3, 4, 5]\nsoma = 0\nfor num in numeros:\n	soma += num\nprint(soma)", ["a) 1", "b) 5", "c) 10", "d) 15"], 4)
pergunta20 = Pergunta(" Qual é o valor final da variável resultado após a execução do seguinte código?\n\nresultado = 1\nfor i in range(1, 6):\n	resultado *= i\nprint(resultado)", ["a) 15", "b) 120", "c) 720", "d) 6"], 2)

#jogo
game = Game([pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, pergunta6, pergunta7, pergunta8, pergunta9, pergunta10, pergunta11, pergunta12, pergunta13, pergunta14, pergunta15, pergunta16, pergunta17, pergunta18, pergunta19, pergunta20])

#botao Sair do jogo e voltar pra tela de login

def sair():    
    root.destroy()
    import menu_principal

sair_img=tk.PhotoImage(file=r"G:\Meu Drive\Python\PI\Imagens\sair.png")
botao_sair=tk.Button(root, image=sair_img, bg="#0557e4", bd=0, command=sair)
botao_sair.place(x=1100, y=470)


root.mainloop()
