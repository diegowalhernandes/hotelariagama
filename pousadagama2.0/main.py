import mysql.connector
from mysql.connector import Error
nome = []
quarto = []
cpf = []
telefone = []
dias = []
valor_total = []

opcao = 0
cont = 1000
while opcao != 4:
	print("=-"*15)
	print("=-=-Pousada Gama-=-=")
	print("=-"*15)
	opcao = str(input("""
	[1] Reservar
	[2] Check-in
	[3] Check-out"
	[4] Sair
	Escolha uma opção: """))


	if opcao == '1':
		nome = str(input("Nome: "))
		cpf = int(input("CPF: "))
		telefone = int(input("Telefone: "))
		dias = int(input("Quantos dias deseja ficar: "))
		quarto = str(input("Escolha um quarto: "))
		valor_total = dias * 50
		cont = cont + 1


		dados = (f"""
		ola {nome},
		seu codidgo é {cont}
		seu cpf é {cpf},
		seu telefone é {telefone},
		você ficará {dias} dias,
		seu quarto é { quarto},
		e o valor total da sua hospedagem é R${valor_total}""")
		print(dados)



		#declaracao = """INSERT INTO clientes
		#(nome, cpf, telefone) VALUES ("""
		#sql = declaracao + dados"

	elif opcao == '2':
		cont = int(input("Codigo da reserva: "))
		print(f"{nome}, {cpf}, {telefone}")
		print(f"Seu quarto será {quarto}")
	elif opcao == '3':
		id = ("Codigo de Reserva: ")
		print(f"{nome}, você ficou {dias} dias e o valor será {valor_total}")
		print("Obrigado e volte sempre!!!")
	elif opcao == '4':
		print('Obrigado!!! Pousada Gama')

	#	try:
	#		inserir_clientes = sql
	#		cursor.execute(inserir_clientes)
	#		print(cursor.rowcount, "Registros inseridos na tabela")
	#	except Error as erro:
