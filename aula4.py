nome = 'Thiago Lua'
altura = 1.73
peso = 90
imc = peso / (altura ** 2)

# f-strings
linha1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} kg e seu IMC é {imc:.1f}'

print(linha1)