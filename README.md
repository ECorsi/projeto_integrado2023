# projeto_integrado2023

Passo a passo para que o progma seja executado corretamente:
- Primeiro de tudo o Usuário deve baixar o Mysql.
- Criar um banco de dados com nome: Registro_usuario.
- Criar uma tabela com nome login com o seguinte código:
    CREATE TABLE login (
                        IDUsuario INT AUTO_INCREMENT PRIMARY KEY,
                        Usuario VARCHAR(100) NOT NULL UNIQUE,
                        Senha VARCHAR(100),
                        RA VARCHAR(15) NOT NULL UNIQUE,
                        Nome VARCHAR(40) NOT NULL,
                        Pontuacao INT DEFAULT 0
                          )
- Após isso, o Usuário deve se cadastrar (SÓ É POSSÍVEL SE CADASTRAR COM A CHAVE ADM = 1234), preenchendo todos os campos, Usuario, Senha, Nome e RA.
- Com a conta criada basta fazer login e será redirecionado para o menu principal.
- No Menu Principal o Usuário pode escolher 3 opções; Ver o LEADERBOARD, JOGAR ou SAIR e voltar para tela de login.
- Dentro do jogo, serão realizadas 20 perguntaas, tendo 15 segundos para responder cada uma, caso o tempo se esgote o jogo pula para próxima pergunta e a anterior é descartada.
- Ao final do jogo é éxibido uma mensagem mostrando a quantidade de acertos e a % de acerto em relação ao total de perguntas presentes.
- Para sair do jogo, basta o usuário clicar no icon de sair.
