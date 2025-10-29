import random
'''
----------------------------------------------------
DEFININDOS AS FUNÇÕES DO PROGRAMA
----------------------------------------------------
'''
#RECEBE A QUANTIDADE DE LINHAS E DE COLUNAS JUNTO COM QUAL CARACTERE DEVE SER PREENCHIFO E FAZ UMA MATRIZ COM ISSO
def criar_tabuleiro(n_linhas,n_colunas,preencher):
    '''cria uma lista'''
    matriz = []

    '''cria uma lista de lista'''
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(preencher)         
        matriz.append(linha)

    '''retorna a matriz pronta'''    
    return matriz

#RECEBE UMA MATRIZ E IMPRIME EM FORMA DE TABULEIRO
def mostrar_tabuleiro(matriz):
    '''lendo o tamanho da matriz'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])  

    '''imprime o numero de colunas acima do tabuleiro'''
    for i in range(qtd_colunas+1):
        print(f"-{i}-",end= "\t")
    print("\n")

    '''imprime as linhas tendo no inicio o numero da linha'''
    for i in range(qtd_linhas):
        print(f"-{i+1}-",end= "\t")
        for j in range(qtd_colunas):
            print(f"{matriz[i][j]}\t", end ="")
        print("\n")

#COLOCA UMA BOMBA NO TABULEIRO(-1), E SOMA 1 AS CASAS ADJACENTES CASO NÃO FOREM UMA BOMBA TAMBÉM
def colocar_bomba(matriz):
    '''le o tamanho da matriz'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0]) 

    '''define uma posição aleatoria para por a bomba'''
    new_linha = random.randint(0,qtd_linhas-1)
    new_coluna = random.randint(0,qtd_colunas-1)

    '''se ja tiver uma bomba ali ela chama a função novamente'''
    if matriz[new_linha][new_coluna] == -1:
        return colocar_bomba(matriz)
    
    else:
        '''coloca a bomba'''
        matriz[new_linha][new_coluna] = -1

        '''verificar e somar 1 nas casas laterais'''
        for dx in range(-1,2):
            for dy in range (-1,2):
                try:
                    '''se não tiver uma bomba na casa e a posição acessada tiver dentro dos limites da matriz ele soma 1 à aquela posição'''
                    if matriz[new_linha + dx][new_coluna + dy] != -1 and new_linha + dx in range(0, qtd_linhas) and new_coluna + dy in range(0, qtd_colunas):
                        matriz[new_linha + dx][new_coluna + dy] += 1
                    '''se o "if" não for comprido ele e ignorado'''

                except:
                    pass

    '''retorna a matriz com uma bomba'''
    return matriz

#RECEBE UMA LINHA E UMA COLUNA E COLOCA UMA MARCAÇÃO "M" NO TABULEIRO DO JOGADOR
def marcar_bomba(matriz, linha, coluna):
    '''le a posição da bomba corretamente'''
    linha = linha -1
    coluna = coluna -1
    '''
    verifica se;
    -já não há uma marcação ali
    -se a casa já não foi aberta
    caso passar ela pôe a marcação e retorna a matriz alterada
    '''
    if matriz[linha][coluna] == "M":
        print("Já tem um marcador nessa posição!")

    elif matriz[linha][coluna] != "*":
        print("Essa casa já foi aberta")

    else:
        matriz[linha][coluna] = "M"

    return matriz

#RECEBE UMA LINHA E UMKA COLUNA E RETIRA O MARCADOR DESSE LOCAL
def retirar_marcador(matriz, linha, coluna):
    '''concerta a posição recebida'''
    linha = linha -1
    coluna = coluna -1

    '''verifica se tem um marcador ali e coloca um "*" no lugar, se não tiver o marcador ela da um aviso'''
    if matriz[linha][coluna] == "M":
        matriz[linha][coluna] = "*"

    else:
        print("Não tem um marcador aqui para retirar!")

    return matriz

#ABRE AQUELA CASA, SE FOR UMA BOMBA SAI DO JOGO, SE FOR UM 0 ABRE AS CASAS DO LADO, SE FOR UM MARCADOR NÃO FAZ NADA, E SE FOR UM NUMERO O REVELA
def abrir_casa(matriz_b,matriz_j,linha,coluna):
    
    '''concerta a coordanada'''
    linha = linha -1
    coluna = coluna -1

    '''le a quantidade de linhas e colunas'''
    qtd_linhas = len(matriz_b)
    qtd_colunas = len(matriz_b[0]) 

    if matriz_b[linha][coluna] == -1:
        '''fecha o programa se abrir uma bomba'''
        print("Perdeu,fechando o jogo")
        exit()

    elif matriz_b[linha][coluna] != 0 and matriz_j[linha][coluna] != "M":
        '''se tiver um numero ali, a matriz do jogador passa a ter o mesmo numero que a matriz base marca'''
        matriz_j[linha][coluna] = matriz_b[linha][coluna]
        return matriz_j
    
    elif matriz_j[linha][coluna] ==  "M":
        '''ignora se ter uma marcação ali'''
        return matriz_j
    
    else:
        '''passa o 0 para a matriz do jogador'''
        matriz_j[linha][coluna] = matriz_b[linha][coluna]

        '''percorrer as casas laterais'''
        for dx in range(-1,2):
            for dy in range (-1,2):
                '''se a casa estiver dentro da matriz e não for a casa atual da função ela vai chamar a função abrir recursivamente'''
                try:
                    if linha + dx in range(0, qtd_linhas) and coluna + dy in range(0, qtd_colunas) and matriz_j[linha+dx][coluna+dy] !=0:
                        abrir_casa(matriz_b,matriz_j,linha+1+dx,coluna+1+dy)
                        '''!!!O "+1" serve para anular o "-1" do inicio da função abrir_casa()'''

                except:
                    pass   

        return matriz_j    

#VERIFICA SE O TABULEIRO DO JOGADOR ESTA COM MARCADORES NAS BOMBAS E SE TODAS AS CASAS ESTÃO ABERTAS, SE SIM O JOGO TERMINA
def venceu(matriz_b,matriz_j,qtd):

    '''olha o tamanho da matriz'''
    qtd_linhas = len(matriz_b)
    qtd_colunas = len(matriz_b[0])

    '''auxiliares para o calculo'''
    aux1 = 0
    aux2 = 0

    '''
    percorrendo a matriz
    -conta quantas casas com bombas na matriz base tem marcadores na matriz jogador,
    se essa quantidade for igual a quantidade de bombas, e a matriz do jogador estiver limpa,
    aparece uma mensaguem de vitoria e o jogo acaba
    '''
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):

            if matriz_j[i][j] == "M" and matriz_b[i][j] == -1:
                aux1 +=1
            if matriz_j[i][j] == "*":
                aux2 +=1

    '''verificador'''
    if aux1 == qtd and aux2 == 0:
        print("Venceu!!!")
        exit()

#FUNÇÃO AUXILIAR QUE AJUDA A SABER QUANTOS MARCADORES TEM SOBRANDO PARA O JOGADOR
def contar_marcadores(matriz):

    '''le o tamanho da string'''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
 
    '''variavel que faz a contagem'''
    aux = 0

    '''percorrendo a matriz'''
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if matriz[i][j] == "M":
                aux +=1

    '''retornando o valor'''
    return aux

'''
-----------------------------------------------------------------------
INICIANDO O JOGO
------------------------------------------------------------------------
'''

print("---CAMPO MINADO---")

#IMPRIMINDO AS REGRAS
print("---REGRAS---")
print("1-O jogador deve definir o tamanho do tabuleiro de no maximo 10x10(quantidade de linhas por colunas).")
print("2-O jogador deve escolhar a quantidade de bombas(a quantidade deve estar dentro do limite o tabuleiro).")
print("3-A quantidade de marcadores é igual a das bombas.")
print("4-Para ganhar basta colocar um marcador em cada espaço que tenha uma bomba e ter todas as outras casas abertas.")
input("(PRESSIONE ENTER PARA PROSSEGUIR!)")

#pedindo o tamanho do tabuleiro e a quantidade de bombas
#com verificação se está sendo realmente colocado um inteiro
#e se o numero está dentro do limite

#PEDINDO A QUANTIDADE DE LINHAS
while True:
    try: 
        '''qtd_l = quantidade de linhas'''
        qtd_l = int(input("Defina a quantidade de linhas do tabuleiro:"))
        if qtd_l >= 1 and qtd_l <= 10:
            break
        else:
            print("O numero de linhas deve estar entre 1 e 10!")
    except ValueError:
        print("Valor incorreto, digite um numero inteiro para as linhas!")

#PEDINDO A QUANTIDADE DE COLUNAS
while True:
    try: 
        '''qtd_c = quantidade de colunas'''
        qtd_c = int(input("Defina a quantidade de colunas do tabuleiro:"))
        if qtd_c >= 1 and qtd_c <= 10:
            break
        else:
            print("O numero de colunas deve estar entre 1 e 10!")
    except ValueError:
        print("Valor incorreto, digite um numero inteiro para as colunas!")

#PEDINDO A QUANTIDADE DE BOMBAS
while True:
    try: 
        '''qtd_b = quantidade de bombas'''
        qtd_b = int(input(f"Defina a quantidade de bombas do tabuleiro(máximo de {qtd_l*qtd_c} bombas):"))
        if qtd_b >= 1 and qtd_b <= qtd_l*qtd_c:
            break
        else:
            print(f"O numero de bombas deve estar entre 1 e {qtd_l*qtd_c}!")
    except ValueError:
        print("Valor incorreto, digite um numero inteiro para as bombas!")

#INICIALIZANDO AS MATRIZES E DEFININDO ALGUNS VALORES

'''definindo a quantidade de marcadores disponiveis'''
qtd_m = qtd_b

'''criando o tabuleiro_jogador:todas as casas com '*' no inicio'''
'''criando o tabuleiro_base com valores numericos(bombas iguais a -1 é a quantidade de bombas nas casas proximas)'''
matriz_base = criar_tabuleiro(qtd_l,qtd_c,0)
matriz_jogador = criar_tabuleiro(qtd_l,qtd_c,"*")

'''chamando a fução colocar bombas dentro de um for que pôe a quantidade de bombas'''
for i in range(qtd_b):
    colocar_bomba(matriz_base)

'''
--------------------------------------------------------------------------
WHILE PRINCIPAL DO PROGRAMA
--------------------------------------------------------------------------
'''
#WHILE ONDE O JOGO FUNCIONA
while True:
    
    '''verificar quantidade de marcadores'''
    qtd_m = qtd_b - contar_marcadores(matriz_jogador)

    '''mostrando o tabuleiro'''
    mostrar_tabuleiro(matriz_jogador)
    print(f"Quantidade de bandeiras disponiveis:{qtd_m}")

    '''verificar se ganhou'''
    venceu(matriz_base,matriz_jogador,qtd_b)
    
    #EXIBINDO OPÇÕES
    print("OPÇÕES:Você deve digitar a opção com letras maiusculas!('M', 'A', 'R' ou 'EXIT')")
    print("M-marcar uma bomba")
    print("A-abrir uma casa")
    print("R-retirar bandeiras")
    print("EXIT-fechar o programa")

    '''escolhendo a opção'''
    op = input("Digite um opção:")

    match op:

        #MARCAR CASA DO TABULEIRO
        case "M":

            '''verificando se há marcadores'''
            if qtd_m > 0:

                print("Marcando uma casa:")

                '''pedindo a linha'''
                while True:
                    try: 
                        linha = int(input("Digite a linha da casa:"))
                        if linha >= 1 and linha <= qtd_l:
                            break
                        else:
                            print(f"O numero da linha deve estar entre 1 e {qtd_l}!")
                    except ValueError:
                        print("Valor incorreto, digite um numero inteiro para a linha!")

                '''pedindo a coluna'''
                while True:
                    try: 
                        coluna = int(input("Digite a coluna da casa:"))
                        if coluna >= 1 and coluna <= qtd_c:
                            break
                        else:
                            print(f"O numero da coluna deve estar entre 1 e {qtd_c}!")
                    except ValueError:
                        print("Valor incorreto, digite um numero inteiro para a coluna!")

                '''chamando a função'''
                matriz_jogador = marcar_bomba(matriz_jogador,linha,coluna)
                
                '''caso não houve marcadores'''
            else:
                print("VOCÊ JÁ USOU TODAS AS SUAS BANDEIRAS!!!")

        #ABRIR UMA CASA DO TABULEIRO    
        case "A":
            print("Abrindo uma casa:")

            '''pedindo a linha'''
            while True:
                try: 
                    linha = int(input("Digite a linha da casa:"))
                    if linha >= 1 and linha <= qtd_l:
                        break
                    else:
                        print(f"O numero da linha deve estar entre 1 e {qtd_l}!")
                except ValueError:
                    print("Valor incorreto, digite um numero inteiro para a linha!")

            '''pedindo a coluna'''
            while True:
                try: 
                    coluna = int(input("Digite a coluna da casa:"))
                    if coluna >= 1 and coluna <= qtd_c:
                        break
                    else:
                        print(f"O numero da coluna deve estar entre 1 e {qtd_c}!")
                except ValueError:
                    print("Valor incorreto, digite um numero inteiro para a coluna!")

            '''chamando a função'''
            matriz_jogador = abrir_casa(matriz_base,matriz_jogador,linha,coluna)

        #RETIRAR UM MARCADOR DE UMA CASA
        case "R":
            print("Retirar marcador da casa:")

            '''pedindo a linha'''
            while True:
                try: 
                    linha = int(input("Digite a linha da casa:"))
                    if linha >= 1 and linha <= qtd_l:
                        break
                    else:
                        print(f"O numero da linha deve estar entre 1 e {qtd_l}!")
                except ValueError:
                    print("Valor incorreto, digite um numero inteiro para a linha!")

            '''pedindo a coluna'''
            while True:
                try: 
                    coluna = int(input("Digite a coluna da casa:"))
                    if coluna >= 1 and coluna <= qtd_c:
                        break
                    else:
                        print(f"O numero da coluna deve estar entre 1 e {qtd_c}!")
                except ValueError:
                    print("Valor incorreto, digite um numero inteiro para a coluna!")    

            '''chamando a função'''
            matriz_jogador = retirar_marcador(matriz_jogador,linha,coluna)

        #OPÇÃO DE FECHAR PROGRAMA
        case "EXIT":
            print("Fechando o programa!")
            exit()

        #CASO DE OPÇÃO INVÁLIDA    
        case _:
            print("Opção inválida, tente novamente!(Pressione ENTER para prosseguir)")

            input()
