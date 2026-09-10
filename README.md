




# 🎮 Jogo da Vida — Terminal Adventure Game

🇧🇷 **Português** · [🇺🇸 English](README.en.md)

Um jogo de aventura de texto rodado no terminal, no estilo **"Day in the Life"**: você
acompanha um dia na vida de um personagem e cada escolha (a que horas acordar, o que
comer, como ir para a escola, o que fazer no intervalo) altera três atributos —
**energia**, **fome** e **dinheiro** — até chegar em um de três finais possíveis.

Projeto do **Checkpoint Project** do curso [*The Legend of Python* — Codédex](https://www.codedex.io/),
feito após os quatro primeiros capítulos, usando apenas **variáveis, fluxo de controle e loops**.

<!-- DEMO: arraste o arquivo .mp4 para cá ao editar este README no GitHub.
     O GitHub sobe o vídeo e gera um link user-attachments que toca inline. -->

---

## 🕹️ Como jogar

Requer **Python 3.10+** (não usa nenhuma biblioteca externa).

```bash
python terminal_game.py
```

Digite seu nome e idade e vá escolhendo as opções pelo número correspondente.
O jogo mostra o status (`Energia | Fome | Dinheiro`) ao fim de cada cena.

> Menores de 10 anos não conseguem jogar — o programa encerra na verificação de idade.

---

## 🗺️ Estrutura da aventura

| Cena | Situação | Escolhas | Impacto |
| ---- | -------- | -------- | ------- |
| **1 — Acordar** | O despertador toca | 07h30 / 09h00 / 11h00 | Define a `situacao` do dia (`cedo`, `levemente_atrasado`, `atrasado`) e mexe em energia/fome |
| **2 — Café da manhã** | Cozinha, tempo depende de quando acordou | Cardápio muda conforme a `situacao` (3 opções cada, ou 2 se estiver atrasado) | Reduz fome, ajusta energia e, se atrasado, gasta dinheiro |
| **3 — Ir para a escola** | Escolha do transporte | Ônibus (R$5) / Bicicleta / A pé | Gasta energia e dinheiro; combinado com a `situacao`, decide se `chegou_no_horario` |
| **4 — Intervalo na escola** | Hora do lanche | Cantina (R$10) / Lanche de casa / Cantina barata (R$5) / Não comer / Matar aula | Compras dependem de ter dinheiro suficiente; matar aula custa energia |
| **Evento aleatório** | Chamada surpresa do professor | — (sorteado com `random.choice`) | Quem chegou atrasado leva falta e perde energia |
| **Final** | Fim do dia | — | Um de três desfechos, calculado a partir de `chegou_no_horario`, `energia` e `fome` |

### Finais possíveis

- **"Dia produtivo. Você mandou bem."** — chegou no horário, energia > 50 e bem alimentado (fome < 40)
- **"Começou mal e não recuperou."** — não chegou no horário
- **"Você sobreviveu ao dia, mas de raspão."** — chegou no horário, mas terminou cansado ou com fome

---

## 🧠 Conceitos aplicados

- **Variáveis** e atualização de estado ao longo do programa (`energia`, `fome`, `dinheiro`, `situacao`, `chegou_no_horario`)
- **Fluxo de controle**: `if / elif / else`, condições compostas (`and`, `!=`, `not in`), `if` aninhado
- **Loops**: `while` para validação de entrada — o menu repete até o jogador digitar uma opção válida
- **Booleanos** derivados de condições (`chegou_no_horario = transporte != "3"`)
- **Clamp de valores** com `max(0, min(valor, 100))` para manter os atributos entre 0 e 100
- **Aleatoriedade** com `random.choice([True, False])` para um evento fora do controle do jogador
- `sys.exit()` para encerrar o jogo na verificação de idade
- `time.sleep()` para ritmar a narrativa

---

## 🛠️ Ferramentas

- Python 3
- [Black](https://black.readthedocs.io/) para formatação de código
- Visual Studio Code

---

## 📂 Arquivos

```text
.
├── terminal_game.py   # o jogo
├── README.md           # este arquivo (PT-BR)
└── README.en.md        # versão em inglês
```
