# coding=utf-8
#################################################################################
#
#  Geog Rosa Peralta
#  Ing Gerardo
#
#  Sistemas Dinamicos 1er Parcial
#
#  (a)Haga un programa que genere los numeros de la sucesión de Fibonacci
#  aplicando la ecuacion de recurrencia:
#
#                         Fk+2 = Fk+1 + Fk
#
#  que los define y calcule, con él, los valores de Fk para k = 0,1, ... , 25
#
#  (b) Modifique, si fuere necesario, el programa del inciso anterior para
#  generar la sucesión de números de Lucas que son de la forma:
#
#                         Lk+2 = Lk+1 + Lk
#
#  pero cuyas condiciones iniciales son Lk= 2 y Lk1= 1 y calcule los valores
#  de L k para k = 0,1, ... , 25
#
##################################################################################


sucesion = int(input("Elegir una sucesion: (1)S. de Fibonacci y (2)S. de Lucas: "))

if sucesion == 1:
    Fk = 0
    Fk1 = 1
    fibonacci = [Fk, Fk1]
    fin = int(input("Hasta que numero se calcula: "))
else:
    Fk = 2
    Fk1 = 1
    fibonacci = [Fk,Fk1]
    fin = int(input("Hasta que numero se calcula: "))


# FORMULA ES Fk+2 = Fk+1 + Fk

for fib in range(0,fin-2):
    Fk=fibonacci[fib]
    Fk1=fibonacci[fib+1]
    Fkn= Fk + Fk1
    fibonacci.append(Fkn)
print fibonacci