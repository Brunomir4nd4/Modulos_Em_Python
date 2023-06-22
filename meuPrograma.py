from minhabiblioteca import modulo1
from minhabiblioteca import modulo2

while 1:
    
    switch = int(input("\nExcolha um tipo de conta aritimética \n 1 Fatorial\n 2 Opreções Base\n 0 Sair\n"))
    if switch == 0:
        print("Programa finalizado")
        break

    num = int(input("Digite um número: "))
    
    if switch == 1:
        print(modulo1.fatorial(num))

            
    elif switch == 2:

        num2 = int(input("Digite um segundo número: "))
        subSwitch = int(input(" 1 Soma\n 2 Diferença\n 3 Produto\n 4 Divisão\n"))
        

        if subSwitch == 1:
            print(modulo2.soma(num, num2))

        elif subSwitch == 2:
            print(modulo2.diferenca(num, num2))


        elif subSwitch == 3:
            print(modulo2.produto(num, num2))


        elif subSwitch == 4:
            print(modulo2.divisao(num, num2))
        
        else:
            print("Metodo invalido")
