# if / elif    /else
# se / se nao se  /se nao

entrada = input('voce quer "entrar" ou "sair"? ')

if entrada == "entrar":
    print('voce entrou no sistema')

elif entrada == "sair":
        print("voce saiu do sistema")

else:
      print("voce nao digitou nem entrar e nem sair.")

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')