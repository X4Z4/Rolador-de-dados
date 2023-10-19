import random

numero_de_dados = int(input("Quantos dados você quer rodar? "))
dado = int(input("Quantas faces tem o dado que você quer rodar? "))
dados_rolados = []

def numero_aleatorio():
    return random.randint(1, dado)

for _ in range(numero_de_dados):
    dados_rolados.append(numero_aleatorio())

bonus = input("Você tem bônus? [S] ou [N]: ")

if bonus.lower() in ["s", "sim"]:
    valores_bonus = [int(input(f"Quanto é o valor do bônus para o dado {i+1}? ")) for i in range(numero_de_dados)]
    soma_com_bonus = [dados_rolados[i] + valores_bonus[i] for i in range(numero_de_dados)]
    for i in range(numero_de_dados):
        print(f"O valor do dado {i+1} foi {dados_rolados[i]} e o bônus é {valores_bonus[i]}, a soma é {soma_com_bonus[i]}")
else:
    if numero_de_dados == 1:
        print(f"O valor do dado foi {dados_rolados[0]}")
    else:
        for i in range(numero_de_dados):
            print(f"O valor do dado {i+1} foi {dados_rolados[i]}")
