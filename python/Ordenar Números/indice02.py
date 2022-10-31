indice = []

while True:
    add_indice = input(str("\033[1;36;45m\n STOP para parar \n Adicionar valor: \033[m"))
    add_indice = add_indice.upper()
    if add_indice != ('STOP'):
        indice.append(add_indice)
        continue
    if add_indice == ('STOP'):
        break

num_ordem = sorted(indice)

print(f'Decrescente: {num_ordem[::-1]}')
print(f'Crescente: {num_ordem[::1]}')
arq = open("decrescente2.txt", "w")
arq.write(str(num_ordem[::-1]))
arq.close()
arq = open("crescente.txt2", "w")
arq.write(str(num_ordem))
arq.close()
