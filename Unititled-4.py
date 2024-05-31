def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

def verificar_situacao(media):
    if media == 10:
        print("Parabéns, sua média é 10")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

def main():
    notas = []
    
    while True:
        nota_str = input("Digite uma nota (ou digite 'fim' para encerrar): ")
        if nota_str.lower() == "fim":
            break
        nota = float(nota_str)
        notas.append(nota)
    
    media = calcular_media(notas)
    print("Média:", media)
    verificar_situacao(media)

if __name__ == "__main__":
    main()