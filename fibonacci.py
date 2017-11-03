import numpy as np

Fk = 0
Fk1 = 1
fibonacci = [Fk]
Fkn = 0

# FORMULA ES Fk+2 = Fk+1 + Fk

for fib in range(0,1):
    print ('Fibonacci', fibonacci)
    print ('Fib', fib)
    print ('Fkn', Fkn)
    if Fkn <= 1:
        Fkn = fib + Fk1
        Fk1 = Fkn
        print (Fkn)
        fibonacci.append(Fkn)
    #else:
     #   Fk1 = Fkn
     #   Fkn = Fkn + Fk1
     #   fibonacci.append(Fkn)
     #   print (Fkn)
