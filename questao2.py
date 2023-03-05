def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

num = int(input("Digite um número inteiro: "))

seq_fib = fibonacci(num)

#Verificando se o número pertence
if num in seq_fib:
    print(f"O número {num} pertence à sequência de Fibonacci até o valor {seq_fib[-1]}.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci até o valor {seq_fib[-1]}.")