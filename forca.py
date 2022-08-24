def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    acertou = False
    enforcou = False

    while(not enforcou and not acertou):
        chute = input('qual letra?: ')

        index = 0
        
        for letra in palavra_secreta:
            if(letra == chute ):
                print("Encontrei a letra {} na posição {}".format(letra,index))
            index = index + 1



        print('Jogando...')

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
