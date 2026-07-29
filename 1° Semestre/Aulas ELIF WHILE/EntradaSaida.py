print ( 10 )		# Um número
total = 101.33
print ("O total é: ")	# Um texto
print ( total )		# Uma variável

qtde = 8
print ("Foram comprados %d produtos" %qtde) 

altura = 1.80
nome = "Fulano"
print ("%s tem %f m de altura"  %(nome, altura) ) 

print ("O total foi R$ %.2f "  %total ) 
print ("O total foi R$ %8.2f "  %total ) 
print ("Foram vendidos %05d produtos"  %qtde) 


nome = input ("Informe seu nome: ")
altura = float ( input("Informa sua altura: ") )
qtdeFilhos = int( input("Qtde de filhos: ") )

print ("%s possui %.2f m de altura e %d filhos."  %(nome,altura,qtdeFilhos) )