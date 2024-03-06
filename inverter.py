
# Resolução metodo 1

string = input("Digite a string: ")

print(f"Resolução pelo metodo 1: {string[::-1]}")



# resolução metodo 2

string = input("Digite a string: ")
string_invertida = ''
tam = len(string)  #pega o tamnho da string
string = list(string)  #quebra a string em um vetor de chars
while tam > 0:
    string_invertida = string_invertida + string[tam-1]
    tam = tam -1

print(f"Resolução pelo metodo 2: {string_invertida}")