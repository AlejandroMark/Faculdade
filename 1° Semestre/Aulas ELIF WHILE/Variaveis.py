import math     # inserir biblioteca de funções matemáticas

# VARIÁVEIS
x = 10
y = 45
n1 = 15
n2 = 29
idade = 33
altura = 1.70	#usa ponto para separar decimal
salarioBruto = 5678.99
valor_produto = 17.99

nome = "Jean"
sobreNome = "Glazar"
nome_do_meio = "Eduardo"
string_vazia = ""
string_nao_vazia = " " 	# 1 caracter em branco


# OPERADORES MATEMÁTICOS
n1 = x + y
total = n1 * 2
p1 = total // 3
p2 = p1
p3 = p1 + (total % 3)
print ("P1= %d, P2 = %d, P3 = %d" %(p1,p2,p3) )


# FUNÇÕES MATEMÁTICAS
print ( abs ( -10 ) )     # retorna 10
print ( pow ( 2, 8 ) )    # 2 elevado a 8 ==> 256

print ( round ( 4.7 ) )   # retorna 5
print ( round ( 4.4 ) )   # retorna 4

print ( math.ceil(4.1) )  # retorna 5
print ( math.ceil(4.9) )  # retorna 5

print ( math.floor(4.1) ) # retorna 4
print ( math.floor(4.9) ) # retorna 4

print ( math.sqrt(81) )   #retorna raiz quadrada de 81 ==> 9
print ( math.pi )         # valor de PI


#STRINGS
dia = 18
texto = "Hoje é dia "
dia_texto = str( dia )    # converte 18 em "18"
texto = texto + dia_texto # junta "Hoje é dia " com "18"

print (texto)
print ( len ( texto ) )   # retorna qtde de caracteres ==> 13