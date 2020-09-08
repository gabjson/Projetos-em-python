x = int(input('Digite um numero: '))
f = 0

if x <= 1:
    f = 1
if x <= 2 or x < 1 :
    f = 2
if x <= 3 or  x < 2:
    f = x**2
if x >= 3 :
    f = x **3
    
print(f)
    
