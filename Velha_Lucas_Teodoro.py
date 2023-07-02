import os
import random
import time
from colorama import Fore

jogadas = 0
jogadascpu = 0
quemJoga = 2  # 1=cpu - 2=jogador
maxJogadas = []
vitória = 'n'
jogarNovamente = 's'
velha = []

print(Fore.MAGENTA)

def menu():
    os.system('clear')
    print('''
                        
                        ############### JOGO DA VELHA ###############
                        #                                           #
                        #    1- INICIAR JOGO                        #
                        #    2- INSTRUÇÕES                          #
                        #    3- SAIR                                #
                        #                                           #
                        #############################################    
        ''')
    opcao = input('\t\t\tDIGITE UMA OPÇÃO: ')

    if opcao == "1":
        tela()
    elif opcao == "2":
        os.system('clear')
        print('''\t################################  INSTRUÇÕES DE JOGO  ################################

        - O jogo da velha é um jogo clássico jogado em um tabuleiro;
        - Neste jogo temos as opções 3x3, 5x5, 7x7 e 9x9;
        - Onde dois jogadores alternam entre colocar "X" e "O" em células vazias;
        - O jogador tem como objetivo, conseguir preencher uma linha, coluna ou diagonal.

        ######################################################################################
        ''')
        input("Pressione ENTER para voltar ao MENU...")
        os.system('clear')
        menu()  # Chama novamente o menu após exibir as instruções
    elif opcao == "3":
        os.system('clear')
        print("################################ JOGO ENCERRADO ################################")
        time.sleep(2)
        os.system('clear')
        quit()

def tela():
    global velha
    global jogadas
    global jogadascpu
    os.system('clear')
    print(Fore.MAGENTA)
    print('\t\t\t      ', end='')
    for i in range(len(velha[0])):
        print(i, end='   ')
    print()
    for i, linha in enumerate(velha):
        print('\t\t\t{}:   '.format(i), end='')
        for elemento in linha:
            print(elemento, '|', end=' ')
        print()
        print('\t\t\t     ', end='')
        for _ in linha:
            print('----', end='')
        print()
    print('\n')
    print(Fore.MAGENTA, 'JOGADAS JOGADOR: ', Fore.BLUE, str(jogadas))
    print(Fore.MAGENTA, 'JOGADAS CPU: ', Fore.RED, str(jogadascpu))

def escolher_layout():
    global velha
    global maxJogadas
    os.system('clear')
    print('Loading #')
    time.sleep(1)
    os.system('clear')
    print('Loading ##')
    time.sleep(1)
    os.system('clear')
    print('Loading ###')
    time.sleep(1)
    os.system('clear')
    print('################################ ESCOLHA O LAYOUT DO JOGO ################################')
    print('1. 3x3')
    print('2. 5x5')
    print('3. 7x7')
    print('4. 9x9')
    opcao = input('Digite o número da opção desejada: ')
    if opcao == '1':
        velha = [[' ' for _ in range(3)] for _ in range(3)]
        maxJogadas = 9
    elif opcao == '2':
        velha = [[' ' for _ in range(5)] for _ in range(5)]
        maxJogadas = 25
    elif opcao == '3':
        velha = [[' ' for _ in range(7)] for _ in range(7)]
        maxJogadas = 49
    elif opcao == '4':
        velha = [[' ' for _ in range(9)] for _ in range(9)]
        maxJogadas = 81
    else:
        print('Opção inválida. Escolhendo layout padrão 3x3.')
        velha = [[' ' for _ in range(3)] for _ in range(3)]
    os.system('clear')
    jogar()

def jogar():
    global jogadas
    global jogadascpu
    global quemJoga
    global maxJogadas
    global vitória

    menu()
    #loop principal
    while True:
        tela()
        qtd_jogadas()
        cpu_joga()
        tela()
        vitória = verificar_vitória()
        if vitória != 'n' or jogadas >= maxJogadas:
            break

    print(Fore.GREEN + 'FIM DE JOGO')
    if vitória == 'X' or vitória == 'O':
        print('Resultado: Jogador', vitória, 'Venceu')
    elif jogadas >= maxJogadas:
        print('Resultado: Empate')
    jogarNovamente = input(Fore.MAGENTA + 'Jogar Novamente? [s/n]: ')
    if jogarNovamente == 'n':
        os.system('clear')
        print(Fore.MAGENTA, '################################ JOGO ENCERRADO ################################')
        time.sleep(2)
        os.system('clear')
    reinicializar()

def qtd_jogadas():
    global jogadas
    global jogadascpu
    global quemJoga
    global vitória
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            print(Fore.MAGENTA)
            l = int(input('Linha: '))
            c = int(input('Coluna: '))
            while velha[l][c] != ' ':
                print('Posição ocupada. Tente novamente.')
                l = int(input('Linha: '))
                c = int(input('Coluna: '))
            velha[l][c] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('Linha ou coluna Inválida')
            time.sleep(1)

def cpu_joga():
    global jogadas
    global jogadascpu
    global quemJoga
    global vitória
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randint(0, len(velha)-1)
        c = random.randint(0, len(velha)-1)
        while velha[l][c] != ' ':
            l = random.randint(0, len(velha)-1)
            c = random.randint(0, len(velha)-1)
        velha[l][c] = 'O'
        quemJoga = 2
        jogadascpu += 1

def verificar_vitória():
    global velha
    for linha in velha:
        if linha.count(linha[0]) == len(linha) and linha[0] != ' ':
            return linha[0]

    for coluna in range(len(velha)):
        check = []
        for linha in velha:
            check.append(linha[coluna])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return check[0]

    diagonal1 = []
    for i in range(len(velha)):
        diagonal1.append(velha[i][i])
    if diagonal1.count(diagonal1[0]) == len(diagonal1) and diagonal1[0] != ' ':
        return diagonal1[0]

    diagonal2 = []
    for i in range(len(velha)):
        diagonal2.append(velha[i][len(velha)-i-1])
    if diagonal2.count(diagonal2[0]) == len(diagonal2) and diagonal2[0] != ' ':
        return diagonal2[0]

    return 'n'

def reinicializar():
    global velha
    global jogadas
    global jogadascpu
    global quemJoga
    global maxJogadas
    global vitória
    global jogarNovamente

    jogadas = 0
    jogadascpu = 0
    quemJoga = 2
    maxJogadas = 9
    vitória = 'n'
    velha = []

    jogarNovamente = 's'

    escolher_layout()


escolher_layout()
