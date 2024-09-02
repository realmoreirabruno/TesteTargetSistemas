# Exercicio2
def fibonacci(n):

    if n < 0:
        return False

    a, b = 0, 1

#se o número é 0 ou 1, ele faz parte da sequencia
    if n == a or n == b:
        return True

#gera a sequencia de Fibonacci até encontrar o numero ou passar dele
    while b < n:
        a, b = b, a + b

    return b == n

def main():
    try:
        numero = int(input("Digite um numero: "))
        if fibonacci(numero):
            print(f"{numero} faz parte da sequência de Fibonacci")
        else:
            print(f"{numero} não faz parte da sequência de Fibonacci")
    except ValueError:
        print("Numero invalido!")

if __name__ == "__main__":
    main()