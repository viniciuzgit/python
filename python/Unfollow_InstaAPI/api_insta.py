# Saber quem eu sigo e não me segue de volta

from InstagramAPI import InstagramAPI
import getpass
import time

usuario = input('Usuário: ')
senha = input('Senha: ')

instagram = InstagramAPI(usuario, senha)
instagram.login()

meu_id = instagram.username_id
lista_seguidores = instagram.getTotalFollowers(meu_id)
lista_id_seguidores = []

for user in lista_seguidores:
    lista_id_seguidores.append(user['pk'])

lista_seguindo = instagram.getTotalFollowings(meu_id)

for user in lista_seguindo:
    if not (user['pk'] in lista_id_seguidores):
        do_unf = input('Dar unfollow em: {}? [Y] ou [N]'.format(user['username']))
        do_unf = do_unf.upper()
        if do_unf == 'Y':
            instagram.unfollow(user['pk'])
            time.sleep(2)
        else:
            pass
