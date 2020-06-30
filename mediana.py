# Achando a mediana para dados agrupados com intervalos de classe.
lin= int ( input (" Digite o limite inferior da classe mediana: "))
ff = int ( input (" Digite o total de frequencia absoluta : "))
fant= int ( input (" Digite a frequencia acumulada anterior à classe mediana : "))
fmd= int ( input (" Digite a frequencia absoluta da classe mediana : "))
AP = int ( input (" Digite a amplitude do intervalo da classe mediana : "))

x = (((ff/2)- fant)*AP)/fmd
y = lin
Mediana = y + x

print (" O valor da mediana é : {}".format(Mediana) )
