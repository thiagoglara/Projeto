divisao = 10 / 2  #divisão sempre retorna float
print(divisao)  # Exibe o resultado da divisão

divisao_inteira = 10 // 2  #retorna resultado inteiro
print(divisao_inteira)  # Exibe o resultado da divisão inteira

exponenciacao = 2 ** 3
print (exponenciacao)  # Exibe o resultado da exponenciação

modulo = 10 % 3  # Resto da divisão
print(modulo)  # Exibe o resto da divisão

# precedencia
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta1)

nome = 'Thiago Lua'
altura = 1.73
peso = 90
imc = peso / (altura ** 2)

print(nome, 'tem ', altura, 'de altura, ')
print('pesa ', peso, 'kg' ' e seu IMC é',imc)