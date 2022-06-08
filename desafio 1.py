# Lendo a variável
v = int(input())
# Verificando se é um palíndromo de 1 algarismo
if v < 9:
    print("oba eh um palíndromo")

# Função que inverte o número
def reverso(n):
    # Declaração de variáveis e vendo o tamanho do número
    cont = 0
    # Para ver o tamanho, transforma-se em string o número e usa o método len(..)
    n = str(n)
    tamanho = len(n)
    # Voltando para inteiro
    n = int(n)

    # Aqui vai acontecer um fatiamento do número até que ele seja 0. Assim, será guardado o mesmo de trás para frente
    # na variável "caixa".
    number = n % 10
    n = n // 10
    caixa = number * 10
    while n != 0:
        number2 = n % 10
        n = n // 10
        caixa = caixa + number2
        cont += 1
        if cont == tamanho-1:
            break
        else:
            caixa = caixa * 10
    # Comparando caixa com o número inicialmente lido para ver se é palíndromo
    if caixa == v:
        print("oba eh um palíndromo")

# Chamando a função
reverso(v)