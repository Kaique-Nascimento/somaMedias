#inicialização de variáveis
numerosDigitados = []
contador = 0
soma = 0
media = 0

#laço que executará o programa até que o número 0 seja digitado
while True:

    #analisa se o codigo nao dara erro
    try:
        numero = float(input(f"Digite um número: (0 para fazer o calculo da media)  "))

    #se o valor digitado nao for um numero
    except ValueError:
        print("Digite um número válido!")

        #volta pro começo
        continue
    
    #autoexplicativo
    if numero == 0:
        print(f"Os números digitados: \n-=-=-=-=-=")

        #percorre os numeros digitados
        for numeros in numerosDigitados:

            #mostra numeros digitados
            print(numeros)

            #soma os numeros digitados
            soma+=numeros

            #faz a media entre eles
            media = soma/contador

        print("-=-=-=-=-=")

        #:.2f mostra 2 números depois da vírgula
        print(f"A soma deles é de: {soma:.2f}")
        print(f"A média entre eles é de: {media:.2f}")
        print(f"A quantidade de números digitados foi de: {contador}")
        break

    #continua o código se o numero for diferente de 0

    #soma a quantidade de numeros +1
    contador+=1

    #acrescenta o numero digitado na lista
    numerosDigitados.append(numero)
    
