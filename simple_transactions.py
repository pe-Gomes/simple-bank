menu = """
  ######## MENU ########

  [s] - Saque
  [d] - Depósito
  [e] - Extrato
  [q] - Sair

  ######################
==> Digite a opção desejada: 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
MAX_SAQUES = 3

while True:
  option = input(menu)

  match option:
    case "d":
      amount_deposited = float(input("Informe o valor do depósito: "))
      if amount_deposited > 0:
        saldo += amount_deposited
        extrato += f"Depósito: R$ {amount_deposited:.2f}\n"
        print("Valor depositado")
      else:
        print("Operação falhou! Valor de depósito inválido")
    case "s":
      withdraw = float(input("Informe o valor do saque: "))
      if saldo < withdraw:
        print("Operação falhou! Saldo insuficiente.")
      elif numero_saques >= MAX_SAQUES:
        print("Operação falhou! Você já atingiu o limite de saques")
      elif withdraw > limite:
        print("Operação falhou! O saque é maior do que o limite de R$ 500,00")
      elif withdraw > 0:
        saldo -= withdraw
        numero_saques += 1
        extrato += f"Saque: R$ {withdraw:.02f}"
        print("Valor sacado")
      else:
        print("Operação falhou! Informe um valor válido para o saque")
    
    case "e":
      print("\n************** EXTRATO ***************")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("\n**************************************")
    case "q":
      break