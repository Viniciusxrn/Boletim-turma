def calcular_media(av1,av2,av3):
    return round((av1+ av2 + av3) / 3 , 1)


def situacao(media) :
    if media >= 7:
        return "APROVADO !"
    elif media >= 5:
        return "REPROVADO !"
    else:
        return "RECUPERAÇÃO"