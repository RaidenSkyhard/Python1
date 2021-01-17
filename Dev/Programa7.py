'''
Programa 7
Formateo de de cadenas
Siono
'''

brand = 'Apple'
valorCambio = 1.235235245

mensaje = 'El precio de %s laptop es de %d USD DOLARES y el porcentaje de cambio es de %4.2f USD DOLARES a 1 EURO'%(brand, 1299, valorCambio)

print (mensaje)

'''
Este ejemplo nos permite reemplazar los valores dentro de la cadena con
la expresión 'CADENA'%(VALORES)
%s corresponde a string
%d corresponde a integer
%f corresponde a flotantes
