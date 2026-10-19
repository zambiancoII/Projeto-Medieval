# ⚔️ A Lenda de Oak Heaven

Um jogo de RPG e aventura interativa em modo texto (CLI), desenvolvido em Python para praticar e consolidar conceitos fundamentais de lógica de programação e algoritmos.

---

## 📜 Sobre o Jogo

O jogo se passa na pacata vila de **Oak Heaven**, onde o protagonista cresceu aprendendo o ofício da forja e da caça. Após um evento misterioso acompanhado por uma grande explosão no horizonte, criaturas ameaçadoras começam a invadir a vila. O jogador deve escolher sua arma e combater as ameaças em turnos para garantir sua sobrevivência.

---

## 🚀 Funcionalidades Implementedas

* **Seleção de Armas:** Escolha de equipamento inicial com validação de entrada e atributos de dano base distintos.
* **Sistema de Combate em Turnos:** Lógica de combate dinâmica com cálculo de dano e chances de erro para ambos os lados.
* **Cutscenes Narrativas:** Apresentação da história com controle de ritmo através de pausas e animação dinâmica em **ASCII Art**.
* **Interface CLI Limpa:** Atualização e navegação fluida no terminal limpando a tela a cada ação.

---

## 🛠️ Tecnologias e Conceitos Utilizados

* **Linguagem:** Python 3
* **Módulos Nativos:**
  * `random`: Para geração de valores aleatórios de dano e chances de acerto nos combates.
  * `os`: Para manipulação e limpeza da tela do terminal (`cls` / `clear`).
  * `time`: Para controle de tempo e execução de animações quadro a quadro.
* **Conceitos de Programação:**
  * Funções e Modularização
  * Laços de Repetição (`while`) e Estruturas Condicionais (`if/elif/else`)
  * Manipulação e Formatação de Strings
  * Tratamento básico de entradas do usuário

---

## 🗡️ Armas Disponíveis

| Arma                      | Dano Base máximo |
|                           |                  |
| **Arco**                  |       05         |
| **Espada Curta e Escudo** |       06         |
| **Espada Longa**          |       08         |
| **Machado**               |       12         |

---

## ⚙️ Como Executar o Jogo

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do arquivo e execute o comando:

```bash
python main.py
```

---

## 📌 Próximos Passos & Melhorias (Roadmap)

- [ ] Integrar a chamada do combate ao final da introdução narrativa.
- [ ] Implementar Programação Orientada a Objetos (POO) para entidades (Jogador e Inimigos).
- [ ] Criar sistema de inventário e poções de cura.
- [ ] Salvar e carregar progresso em arquivo externo (`.txt` ou `.json`).