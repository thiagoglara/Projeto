# if / elif    /else
# se / se nao se  /se nao


primeiro_valor = input('Digite um valor: ')
segundo_valor = input("Digite um segundo valor: ")
if primeiro_valor > segundo_valor:
    print(primeiro_valor, ' é maior que segundo valor ', segundo_valor)
if segundo_valor > primeiro_valor:
    print(segundo_valor, "é maior que primeiro_valor ", primeiro_valor)
elif primeiro_valor == segundo_valor:
    print("Os valores são iguais")

