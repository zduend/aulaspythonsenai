turno = input("Qual turno você estuda?: ")
match turno:
    case "m"|"M":
        print("Bom dia!")
    case "v"|"V":
        print("Boa tarde!")
    case "n"|"N":
        print("Boa noite!")
    case _:
        print("Turno inválido!")
