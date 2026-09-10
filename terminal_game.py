import time
import random
import sys

energia = 100
dinheiro = 25
fome = 90

# ── CENA 1: acordando ──────────────────────────────


print("Seja bem vindo ao Jogo da Vida")
time.sleep(2)
nome = input("Insira seu nome: ")
idade = int(input("Insira a sua idade: "))
if idade < 10:
    print("Esse jogo não é permitido para menores de 10 anos")
    sys.exit()
else:
    print("Hora de acordar...")
time.sleep(2)
print("Sua energia: ", energia)
time.sleep(1)
player_select = ""
while player_select not in ("1", "2", "3"):
    player_select = input(
        "Selecione o horário que você deseja"
        " acordar:\n\n1) 07h30\n2) 09h00\n3) 11h00\n "
    )
    if player_select not in ("1", "2", "3"):
        print("seleção inválida, tente novamente.")
if player_select == "1":
    print(f"Bom dia! {nome} Você acordou cedo")
    energia = energia - 5
    situacao = "cedo"
elif player_select == "2":
    print(f"Eita {nome}! Você dormiu demais...")
    fome = fome + 5
    situacao = "levemente_atrasado"
elif player_select == "3":
    print(f"Corra para se arrumar {nome}! Você está atrasado!")
    energia = energia - 20
    fome = fome + 8
    situacao = "atrasado"


print()
print("Energia:", energia, "| Fome:", fome, "| Dinheiro:", dinheiro)


# ── CENA 2: café da manhã ──────────────────────────────
print()
print("Você corre para a cozinha.")
time.sleep(1)

cafe = ""
if situacao == "cedo":
    print("Tem tempo de sobra. O que você come?")
    print("1) Café reforçado (ovos, pão, cuscuz, achocolatado)")
    print("2) Panqueca com mel")
    print("3) Vitamina de banana")

    while cafe not in ("1", "2", "3"):
        cafe = input("Escolha: ")
        if cafe not in ("1", "2", "3"):
            print("Opção inválida, tente novamente.")

    if cafe == "1":
        print("Você come tudo com calma. Dia começa bem.")
        fome = fome - 60
        energia = energia + 15
    elif cafe == "2":
        print("Panqueca gostosa, mas te deixou meio pesado.")
        fome = fome - 45
        energia = energia + 5
    elif cafe == "3":
        print("Leve e nutritivo.")
        fome = fome - 35
        energia = energia + 20

elif situacao == "levemente_atrasado":
    print("Precisa ser rápido, o ônibus não espera.")
    print("1) Pão com ovo")
    print("2) Torrada com café")
    print("3) Só um achocolatado")

    while cafe not in ("1", "2", "3"):
        cafe = input("Escolha: ")
        if cafe not in ("1", "2", "3"):
            print("Opção inválida, tente novamente.")

    if cafe == "1":
        print("Comeu meio na correria, mas segura até o almoço.")
        fome = fome - 40
    elif cafe == "2":
        print("Rápido e simples.")
        fome = fome - 25
    elif cafe == "3":
        print("Pouca coisa, vai bater fome antes do meio-dia.")
        fome = fome - 15
        energia = energia - 5


elif situacao == "atrasado":
    print("Sem tempo pra nada. O que você faz?")
    print("1) Agarrar uma fruta e sair correndo")
    print("2) Sair sem comer nada")
    cafe = ""
    while cafe not in ("1", "2"):
        cafe = input("Escolha: ")
        if cafe not in ("1", "2"):
            print("Opção inválida, tente novamente.")
    if cafe == "1":
        fome = fome - 15
        energia = energia - 5
    else:
        fome = fome + 5
    dinheiro = dinheiro - 15  # ainda vai ter que comprar na cantina

energia = max(0, min(energia, 100))
fome = max(0, min(fome, 100))
dinheiro = max(0, dinheiro)
print()
time.sleep(1)
print("Energia:", energia, "| Fome:", fome, "| Dinheiro:", dinheiro)

# ── CENA 3: sair de casa ──────────────────────
print("Você sai de casa e vai para a escola.")
time.sleep(1)
print("Escolha seu método de transporte:")
print("1) Ônibus (custa R$5,00 e gasta 10 de energia)")
print("2) Bicicleta (gasta 20 de energia)")
print("3) A pé (gasta 30 de energia)")
transporte = ""
while transporte not in ("1", "2", "3"):
    transporte = input("Escolha: ")
    if transporte not in ("1", "2", "3"):
        print("Opção inválida, tente novamente.")

if transporte == "1":
    print("Você decidiu ir de ônibus.")
    energia = energia - 10
    dinheiro = dinheiro - 5
    fome = fome + 5
elif transporte == "2":
    print("Você decidiu ir de bicicleta.")
    energia = energia - 20
    fome = fome + 10
elif transporte == "3":
    print("Você decidiu ir a pé.")
    energia = energia - 30
    fome = fome + 15

chegou_no_horario = False
if situacao == "cedo":
    chegou_no_horario = True
elif situacao == "levemente_atrasado":
    chegou_no_horario = transporte != "3"
elif situacao == "atrasado":
    chegou_no_horario = transporte == "2"

if chegou_no_horario:
    print("Você chegou na escola a tempo.")
else:
    print("Você chegou atrasado. O portão já estava fechando.")
    energia = energia - 10

energia = max(0, min(energia, 100))
fome = max(0, min(fome, 100))
dinheiro = max(0, dinheiro)

print()
print("Energia:", energia, "| Fome:", fome, "| Dinheiro:", dinheiro)

# ── CENA 4: na escola ──────────────────────
print("Você está na escola. Hora de estudar!")
time.sleep(1)
print("Hora do intervalo")
print("Você tem algumas opções para o intervalo:")
intervalo = ""
print("1) Comprar lanche na cantina (R$10)")
print("2) Comer o lanche que trouxe de casa")
print("3) Lanche barato na cantina (R$5)")
print("4) Não comer nada")
print("5) Matar aula")

while intervalo not in ("1", "2", "3", "4", "5"):
    intervalo = input("Escolha: ")
    if intervalo not in ("1", "2", "3", "4", "5"):
        print("Opção inválida, tente novamente.")
if intervalo == "1":
    if dinheiro >= 10:
        print("Você comprou um lanche na cantina.")
        fome = fome - 30
        dinheiro = dinheiro - 10
    else:
        print("Você não tem dinheiro suficiente para comprar lanche.")
elif intervalo == "2":
    print("Você comeu um lanche que trouxe de casa.")
    fome = fome - 20
elif intervalo == "3":
    if dinheiro >= 5:
        print("Você comprou um lanche barato na cantina.")
        fome = fome - 15
        dinheiro = dinheiro - 5
    else:
        print("Você não tem dinheiro suficiente para comprar lanche barato.")
elif intervalo == "4":
    print("Você não comeu nada.")
    fome = fome + 10
elif intervalo == "5":
    print("Você decidiu matar aula.")
    energia = energia - 20
print("Chegou a hora de ir para casa.")
time.sleep(2)
print()
if random.choice([True, False]):
    print("O professor fez chamada surpresa no fim da aula!")
    if chegou_no_horario:
        print("Você estava presente.")
    else:
        print("Você estava ausente e levou falta.")
        energia = energia - 5
energia = max(0, min(energia, 100))
fome = max(0, min(fome, 100))
dinheiro = max(0, dinheiro)

print()
print("Energia:", energia, "| Fome:", fome, "| Dinheiro:", dinheiro)
if chegou_no_horario and energia > 50 and fome < 40:
    print("Dia produtivo. Você mandou bem.")
elif not chegou_no_horario:
    print("Começou mal e não recuperou. Amanhã é outro dia.")
else:
    print("Você sobreviveu ao dia, mas de raspão.")
