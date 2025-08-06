# operadores in not in

# nome = "otavio"
# print(nome[2])
# print(nome[-5])
# print("a" in nome)
# print("z" in nome)
# print(10 * "-")
# print("vio" not in nome)
# print("a" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar } não está em {nome}')

