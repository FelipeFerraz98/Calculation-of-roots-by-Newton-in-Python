precision = 1e-07

k = 0
x = int(input("Enter a value you want to calculate the root of: ")) #PT: Insira um valor do qual você deseja calcular a raiz:
e = x
i = int(input("Enter an index for the root: ")) #PT: Insira um índice para a raiz:

fx = x**i - e

#Newton's Algorithm for Root Calculation // Algoritmo de Newton para calculo das raizes
while abs(fx) > precision:

    derivativeFX = i*pow(x, i-1)
    x = x - (fx/derivativeFX)
    fx = pow(x, i) - e

    k += 1 #Attempts count // contador de tentativas

    print("\n{}* Result = {:.8f}\n".format(k, x))


print("Final result in {} attempts = {:.8f}".format(k,x))
