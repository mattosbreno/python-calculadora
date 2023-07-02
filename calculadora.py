# 4 operações básicas e função velocidade
def calculadora(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    return soma, subtracao, multiplicacao, divisao

def divisao(num1, num2):
    if num2 == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return num1 / num2

def velocidade(espaco, tempo):
    v = divisao(espaco, tempo)
    return v

# Input dos valores e print do resultado
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = calculadora(num1, num2)
print(f"Soma: {resultado[0]}")
print(f"Subtração: {resultado[1]}")
print(f"Multiplicação: {resultado[2]}")
print(f"Divisão: {resultado[3]}")

espaco = float(input("Digite o espaço percorrido: "))
tempo = float(input("Digite o tempo decorrido: "))

aceleracao = velocidade(espaco, tempo)
print(f"Aceleração: {aceleracao}")
