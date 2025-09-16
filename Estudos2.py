print(12, 34)    #argumentos nao nomeados, a função print le eles e exibe na tela
print(56, 78)

print(12, 34, 59, sep='-')    #o SEP serve para dar um argumento de separação, possibilitando separar com qualquer coisa que esteja entre as ""
print(12, 34, 67, sep="+")

#existem caracteres escondidgos que quebram a linha, no windows é \r\n, \r = return \n = line feed    CRLF   hoje em dia posso usar somente o \n que ja quebra a linha

print(12, 34, 59, sep='-', end='\n')   #por padrao a quebra de linha ja vem automatico mas nao da pra ver
print(12, 34, 59, sep='-', end="ALGO\n")   #posso adicionar algo e fazer a quebra de linha com \n
#e o END serve pra por algo no fim
#vale lembrar que os argumentos vem com = depois deles e posso ultilizar em seguida as "" ou ''