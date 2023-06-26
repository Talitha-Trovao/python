#grupo de entrega:
#Ajailson Castro
#Clebson Farias
#Filipe de Matos
#Isis Suarez
#Talitha Trovao

nivel = input(print('Jogo de adivinhacao. \nEscolha o nivel de dificuldade ou digite s para sair: \n f = facil \n m = medio \n d = dificil\n: \n'))

n_secreto = 50 
pontos = 1000
n_tentativa = 0 #contagem inicial de tentativas para somar até o máximo por nivel

if(nivel == f):
  print('Nível facil. Numero de tentativas = 10.')
  n_tentativa = 10

elif(nivel == m):
  print('Nível medio. Numero de tentativas = 5.')
  n_tentativa = 5

elif(nivel == d):
  print('Nível dificil. Numero de tentativas = 3.')
  n_tentativa = 3

#sair do jogo
elif(nivel == s):
  print('Fim do jogo.')

#limitando os inputs
else:
  print('Comando inválido!')


for rodada in range(1, n_tentativa+1):
  chute = int(input('Qual o o seu chute?\n'))
  if chute > n_secreto:
    print('Seu chute foi maior que o numero secreto. Tentativa {} de {}'.format(rodada, n_tentativa))

  if chute < n_secreto:
    print('Seu chute foi menor que o numero secreto. Tentativa {} de {}'.format(rodada, n_tentativa))

  else:
    print('Número secreto correto! Total de pontos'.format(pontos))

  pontos_erro = pontos - abs(n_secreto - chute)
  pontos = pontos - pontos_erro
