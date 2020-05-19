vidas = 5

arquivo = open('Lista_de_Palavras.txt', 'r')
if arquivo.mode == 'r':
    linhas_do_arquivo = arquivo.readlines()
    for linha in linhas_do_arquivo:
        palavra = linhas_do_arquivo[random.randrange(len(linhas_do_arquivo))]
        palavra = palavra.upper()
arquivo.close()

obscure = "_ "

obscureword = []

for letra in range(len(palavra)-1):
    obscureword.append(obscure)

while vidas > 0: 
    for space in obscureword:
        print(space, end='')

    print('')
    
    letra = input("Digite a letra: ")
    letra = letra.upper()


    for i in range(len(palavra)):
        if palavra[i] == letra:
            obscureword[i] = letra

    for space in obscureword:
        print(space, end='')

    print('')
    letraspalavra = palavra.count(letra)

    if letraspalavra == 0:
        print('Você errou a letra e perdeu uma vida')
        vidas = (vidas - 1)

    print("A palavra contém a letra '" + letra + "'", letraspalavra, 'vez(es).')

    if vidas > 0:
        print("Você ainda tem", vidas, "vidas")
    else:
        print('Você perdeu! :(')
        print('A palavra era', palavra)

    if obscureword == list(palavra[:-1]):
        print('Você venceu!')
        break

    print('')
