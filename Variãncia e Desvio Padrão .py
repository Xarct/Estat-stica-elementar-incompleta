# Medida de dispersão para até 6 valores :
x = float ( input ( " Digite a media aritmética da questão : "))
y = int ( input ( " Digite a quantidade de variaveis ou valores : "))
ax =  int ( input ( " Digite o primeiro valor  : "))
ay =   int ( input ( " Digite o segundo valor  : "))
az =   int ( input ( " Digite o terceiro valor  : "))
aw =  int ( input ( " Digite o quarto valor  : "))
ar =  int ( input ( " Digite o quinto valor  : "))
at = int ( input (" Digite o sexto valor : "))
a = (x - ax)
b = ( x - ay )
c = ( x - az)
d = (x - aw )
e = ( x - ar)
f = (x - at)
V = a**2+ b**2 + c**2 + d**2 + e **2 + f **2
t = abs (V)
Vr = t /y
import math
raiz = math.sqrt (Vr)
print ( " A variancia é de:  {} e o desvio padrão : {}".format (Vr, raiz))