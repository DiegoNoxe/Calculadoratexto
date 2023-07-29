def titulo():
    print()
    print(' | Calculadora a base de texto | ')
    print()
def escolha():
    print()
    from time import sleep
    while True:
     try:
        print('''Escolha a opção abaixo: 
        [1] Soma
        [2] Multiplicação
        [3] Divisão''')
        a = int(input('R: '))
        if a == 1:
          soma()
        elif a == 2:
            mult()
        elif a == 3:
            div()
        else:
            print('Opção invaldia! Tente novamente em 3s')
            sleep(3)
            escolha()
     except ValueError:
         print('Opção invaldia! Tente novamente em 3s')
         sleep(3)
         escolha()
def contador():
    from time import sleep
    print()
    print('Ok, estamos calculando o resultado..')
    sleep(1)
    print('Encontramos o seguinte resultado: ', s)
    print()
def soma():
    global s
    print()
    print('SOMA')
    print()
    n1 = int(input('Escolha o primeiro número: '))
    n2 = int(input('Escolha a segundo número: '))
    s  = n1 + n2
    contador()
def mult():
    global s
    print()
    print('Multiplicação')
    print()
    n1 = int(input('Escolha o primeiro número: '))
    n2 = int(input('Escolha a segundo número: '))
    s  = n1 * n2
    contador()
def div():
    global s
    print()
    print('Divisão')
    print()
    n1 = int(input('Escolha o primeiro número: '))
    n2 = int(input('Escolha a segundo número: '))
    s  = n1 / n2
    contador()
titulo()
escolha()