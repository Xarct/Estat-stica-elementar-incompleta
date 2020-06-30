# Definindo a amplitude  das classes :
x = int ( input ( " Digite o menor valor entre os dados coletados : "))
y = int  ( input ( " Digite o maior valor entre os dados coletados : "))
f = int ( input (" Digite o numero de termos que existem : "))
g = int ( input (" Digite o numero de classes que será organizado : ")) 
AP = ((x - y )/ g)*(-1)
import math
raiz = math.sqrt(f)
if f < 100 :
	print ( AP, ' pelo numero de classes que você deseja ')
	print (raiz, ' pelo metodo de raiz')
else :
	# método strugles para valores maiores 100 :
    import math
    n = 3.3
    l = math.log (f, 10)
    c = 1+(n * l)
    print (c)