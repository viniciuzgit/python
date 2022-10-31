# Lucro por Ação(LA) = Lucro Líquido/Capital Social
# Índice (P/L) = (Preço da Ação na Bolsa) / (LA)
# 

from decimal import Decimal
import datetime
import time

print("\n\033[1;40;41m ÁNALISE FUNDAMENTALISTA \033[m\n")
time.sleep(0.5)
e = str(input("\033[1;40;44mDigite o nome da Empresa:\033[m "))
print('OBS: O NÚMERO INTEIRO SÓ PODE TER UM PONTO PRA INDICAR DECIMAL!')
time.sleep(0.5)
va = Decimal(input("\033[1;40;48mValor da ação:\033[m "))
time.sleep(0.5)
ll = Decimal(input("\033[1;40;44mLucro Líquido: \033[m "))
time.sleep(0.5)
cs = Decimal(input("\033[1;40;48mCapital Social: \033[m "))

la = (ll*1000)/(cs)
pl = va/la

def log():
    now = datetime.datetime.now()
    dia = datetime.datetime.date(now)
    with open(f'Mercado financeiro/analise fundamentalista/files/{e}_{dia}.doc', 'w') as f:
        f.write(f'HORARIO: {now}\n')
        f.write(str(f'{e} - {round(pl)} ANOS\n'))
    return 0

def calculos():
    print(f'\nLucro por Ação {la}')
    print(f'Índice PL {pl}\n')
    print(f'{round(pl)} anos')
    log()
    return 0

calculos()
