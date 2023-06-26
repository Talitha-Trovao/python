#grupo de entrega:
#Ajailson Castro
#Clebson Farias
#Filipe de Matos
#Isis Suarez
#Talitha Trovao



lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

maior = max(lista)
print("Maior numero:", maior)

menor = min(lista)
print("Menor numero:", menor)

pares = [num for num in lista if num % 2 == 0] #varre todos os itens da lista e guarda os que tem resto 0
print("Numeros pares:", pares)

primeiro = lista[0]
qtde_primeiro = lista.count(primeiro)
print("Quantidade de ocorrencias do primeiro elemento:", qtde_primeiro)

media = sum(lista) / len(lista)
print("Media dos numeros:", round(media, 2))

soma_neg = sum([num for num in lista if num < 0])
print("Soma dos numeros negativos:", soma_neg)
