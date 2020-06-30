# Achando a moda pela formula de Czuber - de forma mais cirurgica. Para dados agrupados com intervalos de Classe.
lin= int ( input (" Digte o limite inferior da classe modal:  "))
fmo = int ( input (" Digite a frequencia absoluta da classe modal : "))
fant= int ( input (" Digite a frequencia absoluta anterior à classe modal : "))
fpost = int ( input (" Digite a frequencia absoluta posterior à classe modal : "))
AP = int ( input (" Digite a amplitude do intervalo sa classe : "))

x = fmo - fant
y = 2 * fmo - ( fant + fpost)
Mo = lin + (x*AP/y)

print (" O valor da moda é : {}".format(Mo) )
