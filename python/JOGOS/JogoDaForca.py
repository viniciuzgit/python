from random import randint

def jogar():
  print("***********************************")
  print("    Bem-vindo ao Jogo da Forca     ")
  print("***********************************")

  n = randint(1, 11)
  l = ['banana', 'maçã', 'uva', 'tangerina', 'mamão', 'maracujá', 'morango', 'pera', 'limão', 'laranja']
  palavra_secreta = l[n].upper()
  letras = len(palavra_secreta)
  letras_corretas = ["_"]*letras
  enforcou = False
  acertou = False
  erros = 0

  #enquanto nao enforcou e nao acertou
  while not enforcou and not acertou:
    print(letras_corretas)
    chute = input("Fale uma letra: ")
    chute = chute.strip().upper()

    if chute in palavra_secreta:
      indice = 0
      for letra in palavra_secreta:
        if chute == letra:
          letras_corretas[indice] = letra
        indice = indice + 1
    else:
      erros = erros + 1

    acertou = '_' not in letras_corretas
    enforcou = erros == 6

  if acertou:
    print('A palavra era {}.'.format(letras_corretas))
    print('Parabéns você ganhou!!!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
  else:
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
  print("Fim de jogo.")
jogar()