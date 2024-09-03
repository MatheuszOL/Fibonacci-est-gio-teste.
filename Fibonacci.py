def fibonacci_geral():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_numero(n):
    fib_gen = fibonacci_geral()  # Inicializa o gerador corretamente
    while True: 
        fibonacci_numero = next(fib_gen)
        if fibonacci_numero == n:
            return True
        elif fibonacci_numero > n:
            return False
          
# definindo o número do qual deseja verificar:

numero_para_checar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci_numero(numero_para_checar):  # Chama a função correta
    print(f"O número {numero_para_checar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_para_checar} NÃO pertence à sequência de Fibonacci.") 
    