num = int(input("Digite o numero para saber se é da sequencia de fibonacci: "))

soma = 0
vet= [0,1]

for x in range(num):
    if x ==0:
        soma= vet[x] + vet[x+1]
        vet.append(soma)
    elif x != num:
        soma= vet[x] + vet[x+1]
        vet.append(soma)


print(f"{num} faz parte da sequencia de Fibonacci" if num in vet else f"{num} não faz parte da sequencia de Fibonacci")
