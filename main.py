from datetime import datetime


def inicializar():
    try:
        with open('todo.txt', 'r') as file:
            print('Arquivo encontrado')
            return True
    except IOError:
        try:
            with open('todo.txt', 'a+') as file:
                print('Arquivo criado')
                return True
        except Exception:
            print('Erro desconhecido, tente novamente.')


def ler_lista():
    with open('todo.txt', 'r') as file:
        linhas = file.readlines()
        contador = 0
        text = 'TO-DO LIST'
        print(f'{text.rjust(15)}')
        for c in range(0, len(linhas)):
            contador+=1
            linhas[c] = linhas[c].strip()
            print(f'{contador} {linhas[c]}')


def escrever_elemento(elemento):
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('todo.txt', 'a') as file:
        file.write(now + ' - ' + elemento)


def remover_elemento(elemento):
    with open('todo.txt', 'r') as file:
        linhas = file.readlines()
    with open('todo.txt', 'w') as file:
        contador = 0
        for linha in linhas:
            contador += 1
            if contador != elemento:
                file.write(linha)


programa = inicializar()
while programa:
    print('Digite 1 para ler a lista\nDigite 2 para adicionar\nDigite 3 para remover\nDigite 0 para fechar.\n>>>', end='')
    escolha = int(input())
    if escolha == 1:
        ler_lista()
    elif escolha == 2:
        novo_elemento = str(input('Digite o novo elemento: ') + '\n')
        escrever_elemento(novo_elemento)
    elif escolha == 3:
        ler_lista()
        elemento_escolhido = int(input('Digite o numero correspondente do elemento a ser removido: '))
        remover_elemento(elemento_escolhido)
    elif escolha == 0:
        break
    else:
        print('Digite um numero válido')

print('Fim da aplicação')
