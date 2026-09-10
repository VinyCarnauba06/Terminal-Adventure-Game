# 🎮 Jogo da Vida — Terminal Adventure Game

[🇧🇷 Português](README.md) · 🇺🇸 **English**

A text-based terminal adventure game in the **"Day in the Life"** style: you follow one
day in a character's life, and every choice (what time to wake up, what to eat, how to
get to school, what to do at break) changes three stats — **energy**, **hunger** and
**money** — leading to one of three possible endings.

Built for the **Checkpoint Project** of [*The Legend of Python* — Codédex](https://www.codedex.io/),
after the first four chapters, using only **variables, control flow and loops**.

> The in-game text is in Brazilian Portuguese.

<!-- DEMO: drag the .mp4 file here when editing this README on GitHub.
     GitHub uploads the video and generates a user-attachments link that plays inline. -->

---

## 🕹️ How to play

Requires **Python 3.10+** (no external dependencies).

```bash
python terminal_game.py
```

Enter your name and age, then pick options by their number. The game prints your status
(`Energia | Fome | Dinheiro` = Energy | Hunger | Money) at the end of each scene.

> Players under 10 can't play — the program exits at the age check.

---

## 🗺️ Adventure structure

| Scene | Situation | Choices | Effect |
| ----- | --------- | ------- | ------ |
| **1 — Wake up** | The alarm goes off | 7:30 / 9:00 / 11:00 | Sets the day's `situacao` (`cedo`, `levemente_atrasado`, `atrasado`) and changes energy/hunger |
| **2 — Breakfast** | Kitchen; how much time you have depends on when you woke up | Menu changes with `situacao` (3 options each, or 2 if you're already late) | Lowers hunger, adjusts energy, and costs money if late |
| **3 — Go to school** | Pick your transport | Bus (R$5) / Bike / On foot | Costs energy and money; combined with `situacao`, decides `chegou_no_horario` (arrived on time) |
| **4 — Break at school** | Snack time | Cafeteria (R$10) / Snack from home / Cheap cafeteria (R$5) / Eat nothing / Skip class | Purchases require enough money; skipping class costs energy |
| **Random event** | Pop attendance check by the teacher | — (rolled with `random.choice`) | If you arrived late you're marked absent and lose energy |
| **Ending** | End of the day | — | One of three outcomes, computed from `chegou_no_horario`, `energia` and `fome` |

### Possible endings

- **"Dia produtivo. Você mandou bem."** (*Productive day. Well done.*) — arrived on time, energy > 50, well fed (hunger < 40)
- **"Começou mal e não recuperou."** (*Bad start, never recovered.*) — did not arrive on time
- **"Você sobreviveu ao dia, mas de raspão."** (*You survived the day, but barely.*) — arrived on time but ended tired or hungry

---

## 🧠 Concepts applied

- **Variables** and state updated across the whole program (`energia`, `fome`, `dinheiro`, `situacao`, `chegou_no_horario`)
- **Control flow**: `if / elif / else`, compound conditions (`and`, `!=`, `not in`), nested `if`
- **Loops**: `while` for input validation — the menu repeats until the player enters a valid option
- **Booleans** derived from conditions (`chegou_no_horario = transporte != "3"`)
- **Value clamping** with `max(0, min(value, 100))` to keep stats between 0 and 100
- **Randomness** with `random.choice([True, False])` for an event outside the player's control
- `sys.exit()` to end the game at the age check
- `time.sleep()` to pace the narrative

---

## 🛠️ Tools

- Python 3
- [Black](https://black.readthedocs.io/) for code formatting
- Visual Studio Code

---

## 📂 Files

```text
.
├── terminal_game.py   # the game
├── README.md           # Portuguese (default)
└── README.en.md        # this file (English)
```
