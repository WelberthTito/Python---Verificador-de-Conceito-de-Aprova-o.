

while True: #Indicando o Laço while como True, vai executar o programa Indefinidamente.
    print('Seja bem vindo ao Sistema de Conceito de Aprovação! (S.C.A)') #Apresentação do Programa.
    nomealuno = (input('Digite o seu nome: ')) #O nome do Aluno é armazenado na variavel 'nomealuno' por meio de um input.
    notafinal = float(input('Digite a sua nota Final: ')) #A nota final é convertida de 'String' para 'Real' e armazenada na variavel 'notafinal'.

#Esse Bloco irá Analisar os dados da variavel 'notafinal',e de acordo com a condição classificar o Conceito, imprimindo na tela a mensagem contida na condição.
    if 0 <= notafinal <= 2.9:
        print("O aluno {} tirou nota {} e se enquadra no conceito E ".format(nomealuno, notafinal))
    if 3 <= notafinal <= 4.9:
        print("O aluno {} tirou nota {} e se enquadra no conceito D ".format(nomealuno, notafinal))
    if 5 <= notafinal <= 6.9:
        print("O aluno {} tirou nota {} e se enquadra no conceito C ".format(nomealuno, notafinal))
    if 7 <= notafinal <= 8.9:
        print("O aluno {} tirou nota {} e se enquadra no conceito B ".format(nomealuno, notafinal))
    if 9 <= notafinal <= 10.0:
        print("O aluno {} tirou nota {} e se enquadra no conceito A ".format(nomealuno, notafinal))

  #o bloco a seguir,irá analisar os dados da variável pergunta, se estiver contido a String 'sim', erá continuar normalmente o loop, se estiver Contido a String 'nao', irá encerrar o Programa.

    pergunta = input('Deseja Continuar? s ou n: ')
    if pergunta == 's':
        continue  # Volta ao inicio do loop.
    elif pergunta == 'n':
        print('Encerrando o Programa...Até mais {}'.format(nomealuno))
    break  # Encerra o 'loop'



    #Criado por Welberth Vieira Tito Lima
    # Aluno de Análise e Desenvolvimento De Sistemas - Uninter (2021)
    #20/07/2021
    #email: welberthtito@outlook.com

