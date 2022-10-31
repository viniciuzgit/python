# Cores
RED   = "\033[1;31m"  
GREEN = "\033[0;32m"
AMARELO = "\033[0;33m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

# Design
print('')
print('')
print("""
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗     ██╗██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗    ██║██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║    ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║    ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║    ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═╝
                                                                                                                                                                                                                           
""")

sb = float(input('Salário Bruto: '))

# INSS
if sb > 0 and sb <= 1212:
    aliquota_inss = "7,50%"
    inss = ((7.5/100)*sb)-0
else:
    if sb >= 1212.01 and sb <= 2427.35:
        aliquota_inss = "9%"
        inss = ((9/100)*sb)-18.18
        if inss >= 828.39:
            inss = 828.39
    else:
        if sb >= 2427.36 and sb <= 3641.03:
            aliquota_inss = "12%"
            inss = ((12/100)*sb)-91
            if inss >= 828.39:
                inss = 828.39
        else:
            if sb >= 3641.04 or sb >= 7087.22:
                aliquota_inss = "14%"
                inss = ((14/100)*sb)-163.82
                if inss >= 828.39:
                    inss = 828.39

# dependente é financeiro, financeiramente para sobreviver
dep = int(input('Número de Dependentes: '))
p_aliment = float(input('Pensão Alimentícea: '))
p_priv = float(input('Previdência Privada: '))
outros = float(input('Outras Deduções: '))

# se previdencia priv > multiplicacao de sb por 12%, previdencia = 12%*sb
if p_priv > ((12/100)*sb):
    p_priv = ((12/100)*sb)
    sb12 = p_priv - ((12/100)*sb)
else:
    pass

dependentes = dep*189.59

bc = sb-(inss+p_aliment+p_priv+dependentes+outros)

# IRPF

if bc > 0 and bc <= 1903.98:
    aliquota_ir = "ISENTO"
else:
    pass
if bc >= 1903.99 and bc <= 2826.65:
    aliquota_ir = "7,5%"
    ir = ((7.5/100)*bc)-142.80
else:
    pass 
if bc >= 2826.66 and bc <= 3751.05:
    aliquota_ir = "15%"
    ir = ((15/100)*bc)-354.80
else:
    pass 
if bc >= 3751.06 and bc <= 4664.68:
    aliquota_ir = "22,50%"
    ir = ((22.5/100)*bc)-636.13
else:
    pass 
if bc >= 4664.69:
    aliquota_ir = "27,50%"
    ir = ((27.5/100)*bc)-869.36
else:
    pass 
desc = p_priv+p_aliment
s_liq = sb-ir-inss-desc-outros

aliquota_ef_inss = inss/sb 
aliquota_ef_ir = ir/sb

print(GREEN + f"\nSalário Bruto                  :{sb}" + RESET)
print(RED + f"(INSS)                         :%.2f"%inss + RESET)
print(RED + f"(IRPF)                         :%.2f"%ir + RESET)
print(RED + f"(Previdência Privada)          :%.2f"%p_priv + RESET)
print(RED + f"(Pensão Alimentícea)           :%.2f"%p_aliment + RESET)
print(RED + f"(Outros Descontos)             :%.2f"%outros + RESET)

print(RED + f"(Dependentes)                  :{dependentes}" + RESET)
print(GREEN + f"Base de Cálculo IR             :%.2f"%bc + RESET)
print(GREEN + f"Salário Líquido                :%.2f"%s_liq+ RESET)

print()
print()
print(AMARELO + f"Alíquota INSS                 [{aliquota_inss}]" + RESET)
print(AMARELO + f"Alíquota IR                   [{aliquota_ir}]\n" + RESET)

print(AMARELO + f"Alíquota Efetiva INSS         [{aliquota_ef_inss*100}]" + RESET)
print(AMARELO + f"Alíquota Efetiva IR           [{aliquota_ef_ir*100}]" + RESET)
