🎮 Documento de Design do Jogo (GDD) - A Lenda de Oak Heaven
1. Visão Geral
Nome do Projeto: A Lenda de Oak Heaven

Gênero: RPG de Texto com Escolhas Narrativas e Combate em Turnos (CLI - Terminal)

Linguagem / Tecnologias: Python 3 (random, os, time)

Objetivo do Jogo: Conduzir o protagonista por uma narrativa imersiva na vila de Oak Heaven, onde suas escolhas definem caminhos alternativos e os combates exigem o gerenciamento de atributos estruturados.

2. Conceitos de Programação Aplicados
Dicionários (Substitutos de struct): Modelagem de dados para unificar a "ficha" do jogador e dos inimigos em estruturas de chave-valor.

Modularização Avançada: Organização do projeto dividindo responsabilidades entre o script principal (main.py), lógica de combate (combate.py) e arquivos de história separados por mini-capítulos (capitulos/).

Estruturas de Decisão & Laços: Uso de while para turnos de combate e if/elif/else para direcionamento da narrativa e validações.

Manipulação de Terminal: Animação em ASCII art e controle de tempo com os.system e time.sleep.

3. Arquitetura & Mecânicas do Jogo
📁 Estrutura de Pastas e Arquivos
Para manter o código limpo (evitando o famoso "código linguição"), o projeto será dividido da seguinte forma:

main.py (O "Maestro" — gerencia o fluxo geral e chama os módulos).

combate.py (Contém a lógica de armas, turnos e cálculos de dano).

historia/ (Pasta contendo os mini-capítulos em arquivos separados, ex: cap_1_1.py, cap_1_2.py).

👤 Estrutura da Ficha (Dicionários)
Atributos centralizados em estruturas dinâmicas para fácil manipulação:

Python
# Ficha do Jogador
jogador = {
    "nome": "Rafael",
    "arma": "Machado",
    "dano_base": 12,
    "hp_max": 50,
    "hp_atual": 50
}

# Ficha de Inimigo
inimigo = {
    "nome": "Criatura das Sombras",
    "hp_max": 30,
    "hp_atual": 30,
    "dano_max": 8
}
⚔️ Sistema de Batalha & Progressão
A função battle recebe os dicionários e atualiza o HP diretamente neles.

Persistência de HP entre Batalhas: O personagem mantém o estado de vida (hp_atual) entre um combate e outro, exigindo cuidado e uso de itens futuros.

4. Roadmap do Projeto
📌 Fase Atual (MVP - Produto Mínimo Viável)
[x] Introdução com ASCII art para a explosão em Oak Heaven.

[x] Seleção de arma com validação de entrada.

[x] Loop de turno (combate básico).

⏳ Próximos Passos (Foco Atual)
[ ] Refatorar o código para usar dicionários na ficha do jogador e do inimigo.

[ ] Implementar a persistência da vida (o personagem mantém a vida da última batalha).

[ ] Criar um menu de ações no combate (ex: 1 - Atacar, 2 - Tentar Fugir).

[ ] Separar a narrativa atual em mini-capítulos dentro da pasta historia/.

🔮 Ideias Futuras (Backlog de Estudos & Expansão)
[ ] Narrativa Ramificada (Escolhas): Implementar caminhos diferentes na história com base em decisões (ex: "Se escolher ajudar, ir para o arquivo rota_a.py; senão, rota_b.py").

[ ] Inventário: Lista de poções e itens dentro do dicionário do jogador.

[ ] Persistência em Arquivo: Salvar e carregar o progresso do jogo em .txt ou .json.

[ ] POO: Evoluir os dicionários para Classes (class Personagem:) quando for estudar Orientação a Objetos.

[ ] Variedade de Inimigos: Criar dicionários para diferentes tipos de monstros com atributos próprios.