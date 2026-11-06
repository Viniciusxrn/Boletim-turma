def calcular_media(av1, av2, av3):
    return round((av1 + av2 + av3) / 3, 1)


def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"