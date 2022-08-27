import random

def imprime_mensagem_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    
    arquivo = open("palavras.txt","r")
    palavras =[]
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def jogar():

    imprime_mensagem_abertura()    

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    #letras_acertadas = ["_" for letra in palavra_secreta]
    
    
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
