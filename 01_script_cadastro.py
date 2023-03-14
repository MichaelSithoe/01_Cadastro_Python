#!/bin/python3

certs_prices = {"Nome": [], "Valor": []}
ests_list = {"Nome": [],"Sexo": [], "Idade": [], "Cursos": []}
flag_cert = "sim"
flag_ests = "sim"

print ("#" * 25, 'Registo de Certificacoes (Empire)', "#"*25)
while flag_cert.lower() == "sim":
	cert_name = input("Indique o Nome da Certificacao: ")
	cert_price = input("Indique o Valor da Certificacao: ")
	certs_prices["Nome"].append(cert_name)
	certs_prices["Valor"].append(cert_price)
	
	flag_cert = input ('Deseja cadastrar mais certificacoes? (sim/nao): ')
if flag_cert.lower() == 'sim':
	flag_cert = 'sim'
elif(flag_cert.lower() == 'nao'):
	flag_cert = 'nao'	

#Metodo que retorna a idade do estudante

from datetime import date	
def check_idade(nascimento):
	hoje = date.today()
	idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
	return idade
	
#Registo de Estudante	
print ("="*25,"Cadastro de Estudade","="*25)	
while flag_ests.lower() == 'sim':
	import datetime
	est_name = input("Digite o nome: ")
	est_sexo = input('Digite o sexo (m/f): ')
	est_nascimento = input('Digite a Data de Nascimento (DD-MM-AAAA): ')
	dia, mes, ano = map(int, est_nascimento.split('-'))
	data_convertida = datetime.date(ano, mes, dia)
	idade_est = check_idade(data_convertida)
	if idade_est < 18 : 
		print ("Estudante menor de didade")
	else :
		ests_list["Nome"].append(est_name)
		ests_list["Sexo"].append(est_sexo)
		ests_list["Idade"].append(idade_est)
		valor_mensal = input ("Digite o valor da mensalidade pago: ")
		if float(valor_mensal) > 0 :
			print ("Estudante pagou", valor_mensal, "")
	#ests_list["Cursos"].append(certs_prices[])
	flag_ests = input ('Deseja cadastrar outro estudante? (sim/nao): ')	
		
	if flag_ests.lower() == 'sim':
		flag_ests = 'sim'	
	elif(flag_ests.lower() == 'nao'):	
		print ("="*25,"Certificacoes","="*25,"/n",certs_prices,"/n","="*25,"Estudantes","="*25,ests_list)
		
		
