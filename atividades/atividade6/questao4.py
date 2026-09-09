menu = int(input("1 - Mostrar saudação \n2 - Sair do programa\n"))
mostrar = 1
sair = 2

while menu != sair:
    if menu == mostrar:
        print("Olá, seja muito bem-vindo(a)!")
    else:
        print("Opção inválida!")
    menu = int(input("1 - Mostrar saudação \n2 - Sair do programa\n"))
print("Programa encerrado!")






