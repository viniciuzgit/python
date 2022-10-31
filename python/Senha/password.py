
fr = open('Senha/senhas.txt', 'w')

def main():
   password = input("\nPassword: ")
   f = open('Senha/senhas.txt', 'r')
   for word in f:
     if password in f:
      print('Password is correct!')
   else:
      print("Create New Account")
      u = input('User: ')
      s = input("Password: ")
      fr.write(f'User: {u}\nPassword: {s}')
main()