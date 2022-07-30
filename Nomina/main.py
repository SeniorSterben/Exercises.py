import re
name=str(input('Ingrese sus nombres '))
lname=str(input('Ingrese sus apellidos '))
cc=int(input('Ingrese Número de identificación '))
salario=int(input('Ingrese el salario diario '))
dias=int(input('Ingrese los días producidos '))
sueldo=int(salario*dias)
subtrans=float(117100)
salud=int(sueldo*0.4)
pension=int(sueldo*0.4)

to_sueldo=int(sueldo-salud-pension)
sueltrans=int(to_sueldo+subtrans)

print('----------Nomina----------')
print('El/la señor(a):',name,lname)
print('Identificado con número:',cc)
print('Tiene un salario diario de:',salario)
print('Los días que produjo son:',dias)
print('La ganancia es de:',sueldo)
print('Valor dirigido a salud:',salud)
print('Valor dirigido a la pensión:',pension)
if sueldo < 1000000:
  print ('El sueldo total más el subsidio de transporte = ', sueltrans)
elif sueldo == 1000000:
    print('Sueldo total:',to_sueldo)
else:
    print('Sueldo total:', to_sueldo)