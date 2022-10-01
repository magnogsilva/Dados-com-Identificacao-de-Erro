nome = str(input('Digite o seu nome completo: '))
while True:
    try:   
        a_nasc = int(input('Digite o ano de seu nascimento: '))
        if a_nasc > 1922 and a_nasc < 2021:           
            idade = 2022 - a_nasc
            print('O seu nome é {}'.format(nome))
            print('Você tem ou completará {} anos no ano de 2022.'.format(idade))
            break
        else:
            print('Você não digitou o número, ou, digitou um número errado no campo de ano!')
    except:
        print('Você não digitou o número, ou, digitou um número errado no campo de ano!')
