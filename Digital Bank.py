# Criando apresentação

def Apresentacao():
    espacador = '*' * 40
    print(espacador, '\nBoas-vindas ao ProjetoBanco Ana & Larissa\n', espacador, '\nCadastre-se:\n')


Apresentacao()


# Criando classe
# Atributos: Número da conta, nome do titular, saldo disponível
class ContaCorrente():

    # Construtor de classe
    def __init__(self, nome_titular, senha, id_conta, saldo_cc):
        self.nome_titular = nome_titular
        self.senha = senha
        self.id_conta = id_conta
        self.__saldo_cc = 0

    # Métodos: sacar, depositar na Poupança
    def sacar(self):
        valor = int(input('Quanto deseja sacar: R$ '))
        if self.saldo_cc >= valor and self.saldo_cc >= 0:
            self.saldo_cc -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficente.')

    def depositar(self):
        valor = int(input('Quanto deseja depositar: R$ '))
        self.saldo_poup += valor
        print('Depósito realizado com sucesso!')

    def extrato(self):
        espacador = '*' * 20
        print()
        print(espacador)
        print('Titular da conta: ', nome_titular)
        print('Conta Corrente nº: ', id_conta)
        print('Seu saldo atual é R$ ', self.saldo_cc, ',00')
        print(espacador)
        print()

        espacador = '*' * 20
        print(espacador)
        print('Titular da conta: ', nome_titular)
        print('Conta POupança nº: ', id_conta)
        print('Seu saldo atual é R$ ', self.saldo_poup, ',00')
        print(espacador)
        print()

    def get_saldo(self, senha):
        self.senha = senha
        acesso = int(input('Senha: '))
        if self.senha == acesso:
            conta.extrato()
        elif self.senha != acesso:
            print('Acesso negado. Tente novamente.')


# Criando a classe Conta Poupança (sub-classe)
class ContaPoupanca(ContaCorrente):

    def __init__(self, nome_titular, id_conta, saldo_cc, saldo_poup):
        ContaCorrente.__init__(self, nome_titular, senha, id_conta, saldo_cc)
        self.nome_titular = nome_titular
        self.senha = senha
        self.id_conta = id_conta
        self.saldo_cc = 0
        self.saldo_poup = primeiro_dep
        print("Conta cadastrada com sucesso!")

    def resgatar(self):
        valor = int(input('Quanto deseja resgatar: R$ '))
        self.saldo_poup -= valor
        self.saldo_cc += valor
        print('Resgate realizado com sucesso!')


# Solicitando informações iniciais e cadastrando usuário
nome_titular = str(input('Informe seu nome e sobrenome: '))
senha = int(input('Favor cadastrar uma senha de 4 dígitos: '))

import random

id_conta = random.randint(000, 1000)

primeiro_dep = int(input('Seu saldo atual é R$0,00. Realize seu primeiro depósito: R$ '))

conta = ContaPoupanca(nome_titular, id_conta, 0, primeiro_dep)

# Automatizando interação do usuário com a conta
while (True):
    operacoes = int(input(
        'Deseja movimentar sua conta?\nOperações disponíveis (1-Sacar, 2-Depositar, 3-Resgatar, 4-Extrato, 5-Sair): '))

    if operacoes == 1:
        conta.sacar()
    elif operacoes == 2:
        conta.depositar()
    elif operacoes == 3:
        conta.resgatar()
    elif operacoes == 4:
        conta.get_saldo(senha)
    elif operacoes == 5:
        print('Operação finalizada.')
        break
    else:
        print('Valor inválido.')
