import textwrap

def menu():
  menu = """
  ######## MENU ########

  [d]\tDepósito
  [s]\tSaque
  [e]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar Contas
  [nu]\tNovo usuário
  [q]\tSair

  ######################
==> Digite a opção desejada: 
"""
  return input(textwrap.dedent(menu))


def deposit(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Valor depositado")
    else:
       print("Operação falhou! Valor de depósito inválido")
    
    return saldo, extrato

def withdraw(*,saldo, withdraw, numero_saques,limite_saques, limite_valor, extrato):
    if saldo < withdraw:
        print("Operação falhou! Saldo insuficiente.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Você já atingiu o limite de saques")
    elif withdraw > limite_saques:
        print("Operação falhou! O saque é maior do que o limite de R$ 500,00")
    elif withdraw > 0:
        saldo -= withdraw
        numero_saques += 1
        extrato += f"Saque: R$ {withdraw:.02f}"
        print("Valor sacado")
    else:
        print("Operação falhou! Informe um valor válido para o saque")
    return saldo, extrato

def extract(saldo, extrato):
    print("\n************** EXTRATO ***************")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n**************************************")

def list_users(usuarios):
    print("\n************** USUÁRIOS ***************")
    print("Não foram registrados usuários." if not usuarios else usuarios)
    print("\n**************************************")

def list_accounts(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def new_user(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filter_users(cpf, usuarios)
    
    if usuario:
        return print("Já exister usuário com este CPF")
    
    name = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd-MM-aaaa): ")
    telefone = input("Digite o telefone do usuário: ")
    
    usuarios.append({"name": name, "cpf": cpf, "data_nascimento": data_nascimento, "telefone": telefone })
    print("Usuário cadastrado com sucesso")
    
def filter_users(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
        else:
            return None

def new_account(usuarios, agencia, numero_conta):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filter_users(cpf, usuarios)
    
    if usuario == None:
        print("Cadastro do usuário não encontrado")
        return None
    
    print("Conta criada com sucesso!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario }


def main():
    MAX_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        option = menu()
        match option:
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = deposit(saldo, valor, extrato)
            case "s":
                saque = float(input("Informe o valor do saque: "))
                saldo, extrato = withdraw(
                    saldo=saldo,
                    withdraw=saque,
                    numero_saques=numero_saques,
                    limite_saques=MAX_SAQUES,
                    extrato=extrato,
                    limite_valor=limite
                )
            case "e":
                extract(saldo, extrato)
            case "nu":
                new_user(usuarios)
            case "na":
                numero_conta = len(contas) + 1
                conta = new_account(usuarios, AGENCIA, numero_conta)
                if conta: 
                    contas.append(conta)
            case "lu":
                list_users(usuarios)
            case "lc":
                list_accounts(contas)
            case "q":
                break
        
main()