def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input('qual letra?: ')
        chute = chute.strip().upper()

        index = 0
        
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(letra == chute):
                    print("Encontrei a letra {} na posição {}".format(letra,index))
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1
            print('você errou. Faltam {} tentativas'.format(6-erros))

        enforcou = (erros == 6)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


        print('Jogando...')

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
