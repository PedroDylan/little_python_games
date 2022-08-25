def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input('qual letra?: ')
        chute = chute.strip()

        index = 0
        
        for letra in palavra_secreta:
            if(letra.upper() == chute.upper() ):
                print("Encontrei a letra {} na posição {}".format(letra,index))
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)


        print('Jogando...')

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
