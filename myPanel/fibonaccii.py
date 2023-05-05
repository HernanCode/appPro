#Función que no tiene nada que ver con el proyecto pero que la utilize para aprender como funciona la recursividad (ejercicio plus +2 puntos) 
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(35))
