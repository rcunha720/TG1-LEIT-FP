#Bibliotecas Externas
import os
import random
import time

#Limpar a tela do terminal
def clear():
    os.system('cls')

#Saudações e escolha do nome
clear()
print(
"""
+==================================+
| \033[33mBem vindo ao algoritimo do\033[m       |
| \033[33mjogo das damas.\033[m                  |
+==================================+
""")

time.sleep(2)

print("\033[2;32mVamos começar...\033[m")
time.sleep(1)
print("\033[2;32mBoa sorte!\033[m")
time.sleep(2)

#Limpar a tela do terminal
os.system('cls')

time.sleep(1)
j1 = input("Introduz o nome do Jogador 1: ")
j2 = input("Introduz o nome do Jogador 2: ")

#Inicio das peças pretas
clear()
print("\033[33;40mMuito bem! Agora que já registaste o nome dos jogadores, vamos ver quem vai jogar primeiro.\033[m")
time.sleep(2)
print("\033[33;40mNo jogo das damas as peças pretas são as primeiras a começar.\033[m")
time.sleep(2)
print()
print("=-" * 50)
print()
escolha_pecas = input("Queres escolher quem vai ficar com as peças pretas? (S/N) ").upper()

#Escolha voluntária do primeiro jogador
if escolha_pecas == "S" or escolha_pecas == "SIM":
    while True:
        clear()
        print("Nesse caso, escolhe o jogador que queres que comece...")
        ji = input("Podes escrever tanto o \033[33mNOME\033[m como o \033[33mNÚMERO\033[m de jogador: ")
        if ji == "1" or ji == j1 or ji == j1.upper() or ji == j1.lower():
            clear()
            jogador_inicial = 1
            print("Estrutura do jogo: número de peça a jogar[][] número para onde queres jogar[][]")
            print("\033[30;43mEx: [0][2][1][3]\033[m")
            print()
            print("Primeiro jogador a começar: " + str(j1))
            input("Prime \033[4;32mENTER\033[m para começar a jogar. ")
            break
        elif ji == "2" or ji == j2 or ji == j2.upper() or ji == j2.lower():
            clear()
            jogador_inicial = 2
            print("Estrutura do jogo: número de peça a jogar[][] número para onde queres jogar[][]")
            print("Ex: [0][2][1][3]")
            print("Primeiro jogador a começar: " + str(j2))
            input("Prime ENTER para começar a jogar. ")
            break
        else:
            continue

#Sorteio do primeiro jogador
else:
    clear()
    print("Ok! Nesse caso vamos fazer um sorteio...")
    time.sleep(2)
    print("Vamos ver quem vai ficar com as peças pretas")
    time.sleep(2)
    print("Saberás o resultado em:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    jogador_inicial = random.randint(1, 2)
    clear()
    print("Estrutura do jogo: número de peça a jogar[][] número para onde queres jogar[][]")
    print("Ex: [0][2][1][3]")
    if jogador_inicial == 1:
        print("Primeiro jogador a começar: " + str(j1))
        input("Prime ENTER para começar a jogar. ")
    else:
        print("Primeiro jogador a começar: " + str(j2))
        input("Prime ENTER para começar a jogar. ")

#Criação do tabuleiro sem peças
tabuleiro = []
for i in range(8):
    r = ['V' for i in range(8)]
    tabuleiro.append(r)

def pecas_inciais():
    #Criar peças pretas
    tabuleiro[0][0] = 'P'
    tabuleiro[0][2] = 'P'
    tabuleiro[0][4] = 'P'
    tabuleiro[0][6] = 'P'
    tabuleiro[1][1] = 'P'
    tabuleiro[1][3] = 'P'
    tabuleiro[1][5] = 'P'
    tabuleiro[1][7] = 'P'
    tabuleiro[2][0] = 'P'
    tabuleiro[2][2] = 'P'
    tabuleiro[2][4] = 'P'
    tabuleiro[2][6] = 'P'

    #Criar peças brancas
    tabuleiro[7][1] = 'B'
    tabuleiro[7][3] = 'B'
    tabuleiro[7][5] = 'B'
    tabuleiro[7][7] = 'B'
    tabuleiro[6][0] = 'B'
    tabuleiro[6][2] = 'B'
    tabuleiro[6][4] = 'B'
    tabuleiro[6][6] = 'B'
    tabuleiro[5][1] = 'B'
    tabuleiro[5][3] = 'B'
    tabuleiro[5][5] = 'B'
    tabuleiro[5][7] = 'B'

pecas_inciais()

#Visualização do tabuleiro
def mostrar_tabuleiro():
    for i in range(7, -1, -1):
        print(8*"+++++ ")
        print("+ " + str(tabuleiro[i][0]) + " + + " + str(tabuleiro[i][1]) + " + + " + str(tabuleiro[i][2]) + " + + " + str(tabuleiro[i][3]) + " + + " + str(tabuleiro[i][4]) + " + + " + str(tabuleiro[i][5]) + " + + " + str(tabuleiro[i][6]) + " + + " + str(tabuleiro[i][7]) + " + ")
    print(8*"+++++ ")

#Algoritmo de jogadas
def jogada(xantes, yantes, xdepois, ydepois):
    #Jogada Brancas
    if contador % 2 == 0:
        #Verificar que as peças são brancas
        if tabuleiro[xantes][yantes] != 'B' and tabuleiro[xantes][yantes] != 'RB':
            return False
        #Verificar que o espaço para onde a peça vai está vazio
        elif tabuleiro[xdepois][ydepois] != 'V':
            return False
        else:
            #Jogada Normal
            if (xdepois == xantes - 1 and ydepois == yantes - 1) or (xdepois == xantes - 1 and ydepois == yantes + 1):
                return True
            #Eliminação de uma peça na diagonal esquerda
            elif (xdepois == xantes - 2 and ydepois == yantes - 2):
                if (tabuleiro[xantes-1][yantes-1] == 'P' or tabuleiro[xantes-1][yantes-1] == 'RP'):
                    if tabuleiro[xdepois][ydepois] == 'V':
                        tabuleiro[xantes-1][yantes-1] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de uma peça na diagonal direita
            elif (xdepois == xantes - 2 and ydepois == yantes + 2):
                if (tabuleiro[xantes-1][yantes+1] == 'P' or tabuleiro[xantes-1][yantes+1] == 'RP'):
                    if tabuleiro[xdepois][ydepois] == 'V':
                        tabuleiro[xantes-1][yantes+1] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de duas peças na diagonal esqurda
            elif (xdepois == xantes - 4 and ydepois == yantes - 4):
                if ((tabuleiro[xantes-1][yantes-1] == 'P' or tabuleiro[xantes-1][yantes-1] == 'RP') and (tabuleiro[xantes-3][yantes-3] == 'P' or tabuleiro[xantes-3][yantes-3] == 'RP')):
                    if (tabuleiro[xantes-2][yantes-2] == 'V' and tabuleiro[xantes-4][yantes-4] == 'V'):
                        tabuleiro[xantes-1][yantes-1] = 'V'
                        tabuleiro[xantes-3][yantes-3] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de duas peças na diagonal direita
            elif (xdepois == xantes - 4 and ydepois == yantes + 4):
                if((tabuleiro[xantes-1][yantes+1] == 'P' or tabuleiro[xantes-1][yantes+1] == 'RP') and (tabuleiro[xantes-3][yantes+3] == 'P' or tabuleiro[xantes-3][yantes+3] == 'RP')):
                    if (tabuleiro[xantes-2][yantes+2] == 'V' and tabuleiro[xantes-4][yantes+4] == 'V'):
                        tabuleiro[xantes-1][yantes+1] = 'V'
                        tabuleiro[xantes-3][yantes+3] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    #Jogada Pretas
    elif contador % 2 == 1:
        #Verificar que as peças são pretas
        if tabuleiro[xantes][yantes] != 'P' and tabuleiro[xantes][yantes] != 'RP':
            return False
        #Verificar que o espaço para onde a peça vai está vazio
        elif tabuleiro[xdepois][ydepois] != 'V':
            return False
        else:
            #Jogada Normal
            if (xdepois == xantes + 1 and ydepois == yantes + 1) or (xdepois == xantes + 1 and ydepois == yantes - 1):
                return True
            #Eliminação de uma peça na diagonal esquerda
            elif (xdepois == xantes + 2 and ydepois == yantes - 2):
                if(tabuleiro[xantes+1][yantes-1] == 'B' or tabuleiro[xantes+1][yantes-1] == 'RB'):
                    if tabuleiro[xdepois][ydepois] == 'V':
                        tabuleiro[xantes+1][yantes-1] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de uma peça na diagonal direita
            elif (xdepois == xantes + 2 and ydepois == yantes + 2):
                if(tabuleiro[xantes+1][yantes+1] == 'B' or tabuleiro[xantes+1][yantes+1] == 'RB'):
                    if tabuleiro[xdepois][ydepois] == 'V':
                        tabuleiro[xantes+1][yantes+1] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de duas peças na diagonal esquerda
            elif (xdepois == xantes + 4 and ydepois == yantes - 4):
                if((tabuleiro[xantes+1][yantes-1] == 'B' or tabuleiro[xantes+1][yantes-1] == 'RB') and (tabuleiro[xantes+3][yantes-3] == 'B' or tabuleiro[xantes+3][yantes-3] == 'RB')):
                    if (tabuleiro[xantes+2][yantes-2] == 'V' and tabuleiro[xantes+4][yantes-4] == 'V'):
                        tabuleiro[xantes+1][yantes-1] = 'V'
                        tabuleiro[xantes+3][yantes-3] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            #Eliminação de duas peças na diagonal direita
            elif (xdepois == xantes + 4 and ydepois == yantes + 4):
                if((tabuleiro[xantes+1][yantes+1] == 'B' or tabuleiro[xantes+1][yantes+1] == 'RB') and (tabuleiro[xantes+3][yantes+3] == 'B' or tabuleiro[xantes+3][yantes+3] == 'RB')):
                    if (tabuleiro[xantes+2][yantes+2] == 'V' and tabuleiro[xantes+4][yantes+4] == 'V'):
                        tabuleiro[xantes+1][yantes+1] = 'V'
                        tabuleiro[xantes+3][yantes+3] = 'V'
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


#contador com a vez do jogador
contador = jogador_inicial

#Jogadas
#Loop de jogo
while True:
    if contador % 2 == 1:
        #Loop jogadas pretas
        while True:
            clear()
            print("Jogador 1: " + str(j1))
            print("Peças Pretas")
            mostrar_tabuleiro()
            print()
            jogadastring = input("Joga: ")
            lista_jogada = list(jogadastring)
            if (len(lista_jogada) == 12) and (lista_jogada[0] and lista_jogada[3] and lista_jogada[6] and lista_jogada[9] == '[') and (lista_jogada[2] and lista_jogada[5] and lista_jogada[8] and lista_jogada[11] == ']'):
                if jogada(int(lista_jogada[1]), int(lista_jogada[4]), int(lista_jogada[7]), int(lista_jogada[10])) == True:
                    cordxantes = int(lista_jogada[1])
                    cordyantes = int(lista_jogada[4])
                    cordxdepois = int(lista_jogada[7])
                    cordydepois = int(lista_jogada[10])
                    print(cordxantes)
                    tabuleiro[cordxantes][cordyantes] = 'V'
                    tabuleiro[cordxdepois][cordydepois] = 'P'
                    break
                else:
                    continue
    else:
        #Loop jogadas brancas
        while True:
            clear()
            print("Jogador 2: " + str(j2))
            print("Peças Brancas")
            mostrar_tabuleiro()
            print()
            jogadastring = input("Joga: ")
            lista_jogada = list(jogadastring)
            if (len(lista_jogada) == 12) and (lista_jogada[0] and lista_jogada[3] and lista_jogada[6] and lista_jogada[9] == '[') and (lista_jogada[2] and lista_jogada[5] and lista_jogada[8] and lista_jogada[11] == ']'):
                if jogada(int(lista_jogada[1]), int(lista_jogada[4]), int(lista_jogada[7]), int(lista_jogada[10])) == True:
                    cordxantes = int(lista_jogada[1])
                    cordyantes = int(lista_jogada[4])
                    cordxdepois = int(lista_jogada[7])
                    cordydepois = int(lista_jogada[10])
                    tabuleiro[cordxantes][cordyantes] = 'V'
                    tabuleiro[cordxdepois][cordydepois] = 'B'
                    break
                else:
                    continue
    contador+=1
