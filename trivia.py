# Jogo Trivia
def StarWars():
    P1 = input("Em que ano foi lançado o primeiro filme de Star Wars no cinema? ")
    P2 = input("Qual o nome do mestre Jedi que é verde e pequeno? ")
    P3 = input("Qual o primeiro nome do protagonista da trilogia original de Star Wars ?")
    P4 = input("O nome do vilão que se veste de preto e tem uma voz metálica é Darth ...")
    P5 = input(
    "Escreva a letra da opção que NÃO é o nome de um título de filme da saga Star Wars. \n "
        "A) ""Uma nova Esperança \n B) O Retorno do Jedi \n C) Os Jedis Contra Atacam ")
    lista_perguntas = [P1, P2, P3, P4, P5]
    # print(lista_perguntas)

    lista_respostas = ["1977", "YODA", "LUKE", "VADER", "C"]
    cont = 0

    for index, elem in enumerate(lista_perguntas):
        if elem.upper() == lista_respostas[index]:
            print("Parabéns! Você é um(a) Nerd Raiz.")
            cont += 1
        else:
            print("Errado. Você é um(a) Nerd Nutella.")
            print("A resposta certa é ", lista_respostas[index])
    print("Total de pontos: ", cont)


StarWars()
