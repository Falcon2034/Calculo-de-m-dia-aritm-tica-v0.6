
print('Calculo de media de aluno v 0.6:') 
print ('Dev by, Falcon')

#nome do aluno
nome_aluno = input('Qual é seu nome?:')

print  ("Digite sua nota (0 a 10) ")

#PRIMEIRA NOTA DO ALUNO

nota_1 = float(input('Digite sua primeira nota:'))

while nota_1>= 11:
		print (f"*****Erro*****{nota_1} esta incorreto!! Digite um numero de 0 a 10 para continuar*****")	
		if nota_1>=10:
			
			nota_1 = float(input (' Digite um numero de 0 a 10 para prosseguir:'))
		


#SEGUNDA NOTA DO ALUNO
								
nota_2 = float(input ('Digite sua segunda nota:'))

while nota_2 >= 11: 
		print (f"*****Erro*****{nota_2} esta incorreto!! Digite um numero de 0 a 10 para continuar*****")	
		if nota_2>=10:
			
			nota_2 = float(input('Digite um numero de 0 a 10 para prosseguir:'))
		
		
#TERCEIRA NOTA DO ALUNO
		
nota_3 = float(input('Digite sua terceira nota:'))

while nota_3>= 11:
		print (f"*****Erro*****{nota_3} esta incorreto!! Digite um numero de 0 a 10 para continuar*****")	
		if nota_3>=10:
			
			nota_3 = float(input (' Digite um numero de 0 a 10 para prosseguir:'))
		
		 
#QUARTA NOTA DO ALUNO

nota_4 = float(input('Digite sua quarta nota:'))

while nota_4>= 11:
		print (f"*****Erro*****{nota_4} esta incorreto!! Digite um numero de 0 a 10 para continuar*****")	
		if nota_4>=10:
			
			nota_4= float(input(' Digite um numero de 0 a 10 para prosseguir:'))
		


#calculo das 4 notas
notas = nota_1 + nota_2 + nota_3 + nota_4

#Resultado da media final ^^
media_f= notas/4

if media_f>=5:
	print (f" Parabens, você foi aprovado(a) com a media {media_f}")
else: 
	print (f"Você foi reprovado(a) com a  {media_f}")
	




