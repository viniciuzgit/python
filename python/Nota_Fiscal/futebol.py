import time

nome = input("Nome Completo: ")
Actual_Time = time.strftime("%I:%M:%S")
print("\n\t\tNota Fiscal")
print("Nome: {}\nHorário Emissão: {}".format(nome, Actual_Time))
