"Banco v1"
#BASE DE DADOS, NÃO ALTERAR
senha_letras = { 'Carlos Pessoa':'EFS', 'Elisa Alves':'FKS','Cristina Macedo': 'OFI',
'Susana Aguiar':'ONS','Glades Mendes': 'PIN','Julio Miranda': 'OFO','José Dirceu':'NYU', 
'Adriano Romeu':'CDS','Cícero Almeida':'OCI', 'Ermes Brandão':'UGA','Sofia de Lima':'FLO',
'Afonso Amerson':'AFO','Claudio de Oliveira':'OTI'}
#uma lista de senhas para checar a conta
#senhas_letras = senha_letras.values()

senha_num = { 'Carlos Pessoa': 123, 'Elisa Alves': 234,'Cristina Macedo': 456, 
'Susana Aguiar': 567, 'José Dirceu': 874, 'Sofia de Lima': 356, 
'Glades Mendes': 345,'Julio Miranda': 847, 'Adriano Romeu': 893,'Cícero Almeida': 856, 
'Ermes Brandão': 845, 'Afonso Amerson': 589,'Claudio de Oliveira': 475 }
#uma lista de senhas para checar a conta
#senhas_num = senha_num.values()

contas = { '3654':'Carlos Pessoa', '6558':'Elisa Alves','4856':'Cristina Macedo',
'5894':'Susana Aguiar','6954':'José Dirceu','3652':'Sofia de Lima','3564':'Glades Mendes',
'1254':'Julio Miranda','6548':'Adriano Romeu', '4878':'Cícero Almeida','4502':'Ermes Brandão',
'4225':'Afonso Amerson', '8459':'Claudio de Oliveira'}

saldo_contas = { 'Carlos Pessoa':'2500', 'Elisa Alves':'5001.60','Cristina Macedo':'3526.65', 
'Susana Aguiar':'4589.12', 'José Dirceu':'959', 'Sofia de Lima':'1365.22', 
'Glades Mendes':'1829.50','Julio Miranda':'782.30', 'Adriano Romeu':'1100','Cícero Almeida':'232', 
'Ermes Brandão':'5212','Afonso Amerson':'6543.40', 'Claudio de Oliveira': '7345'}

#operações que podem ser feitas
def saldo():
    #mostra o saldo da conta 
    saldo = float(saldo_contas.get(nome_login))
    return saldo
def trans():
        flag = "Operação realizada com sucesso"
    #faz uma transferencia de valores entre duas contas
        print('O limite diário para transferências é de R$600')
        conta = str(input('Informe a conta de destino:'))
        if conta in contas:
            #o usuario confirma se a conta está certa ou não
            nome = contas.get(conta)
            print('Conta de destino está em nome de: {}'.format(nome))
            chave = (str(input("Confimar? Sim/Nao ")).lower()).strip()

            if chave == 'sim':
            #saldo da conta da pessoa que vai tranferir
                saldo_da_conta = saldo()
                print(f'O seu saldo é de: R${saldo()}')
                valor = float(input('informe o valor a tranferir: '))
               
                if valor < saldo_da_conta:
                    senha = int(input('Para confirmar a operação digite sua senha numérica: '))
                    if senha != senhanum_usuario:
                            print('Senha incorreta')
                            trans()
                    else:
                        nome_fornecedor = contas.get(login_usuario)
                        saldo_da_conta -= valor
                    #atualiza o valor da conta de fornecedor
                        saldo_contas[nome_fornecedor] = saldo_da_conta
                    #saida é o valor atualizado da conta do recebedor
                        saida = float(saldo_contas.get(nome)) + valor
                        saldo_contas[nome] = saida
                    #só pra bonito tem a flag
                else: 
                    print('O valor informado é maior que o saldo da conta')
                    trans()
            else:
                trans()
        else:
            print('A conta informada não existe, tente novamente\n')
            trans()
        return flag
 #operacao de saque de valores
def saque():
    saldo_da_conta = saldo()
    valor = float(input('Valor a ser sacado: '))
    if valor < 750.01:
        nome_fornecedor = contas.get(login_usuario)
        saldo_da_conta -= valor   
        saldo_contas[nome_fornecedor] = saldo_da_conta
    else: 
        print('O valor não pode ser maior que R$750.00')
        saque()
    #só pra bonito tem a flag
    flag = "Operação realizada com sucesso"
    return flag
def operacao(opt):
    #escolhe o tipo de opção
    if opcao == 1: print(trans())
    elif opcao == 2: print(f'O seu saldo é de: R${saldo()}')
    elif opcao == 3: print(saque())
    return 

def LOGIN():
    global login_usuario 
    global nome_login 
    global senhanum_usuario
    global opcao 
    login_usuario = input('Para iniciar digite seu login\n')
    nome_login = contas.get(login_usuario)
    senhanum_usuario = senha_num[nome_login]
    if login_usuario in contas:
        print('Bem vindo(a) {}'.format(nome_login))
        senha_da_conta =  senha_letras.get(nome_login)
        sletras = input(str('Para continuar digite sua senha de letras\n')).upper()

    #checagem de acesso so sistema
        if sletras == senha_da_conta: 
            print('Oque deseja fazer? ')
            opcao = int(input('1: Tranferência \n'
                '2: Consultar saldo \n'
                '3: fazer um saque (limite de R$750.00)\n'))
            operacao(opcao)
        else:
            print ('SENHA INCORRETA !')
            LOGIN()
    else: 
        print(":/ Ocorreu um erro com seu login ")
        LOGIN()
    despedida = str('Até a próxima :)')
    return  despedida

#sistema de boas vindas
print('Olá')
print('Seja bem vindo ao banco Cup')
print(LOGIN())
#print('Caso ainda não seja nosso cliente, crie uma conta')
