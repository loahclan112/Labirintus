def opcio_valasztas(dontes_leiras: str, opcio_lista: list[str]) -> str:
    valasztas: str = ""
    print(dontes_leiras)
    if len(opcio_lista) == 0:
        return valasztas
    if len(opcio_lista) == 1:
        return opcio_lista[0]

    while valasztas == "":
        valasztas = input(f"Válassz: {opcio_lista}")
        for valasz_lehetoseg in opcio_lista:
            if valasztas.lower() == valasz_lehetoseg.lower():
                return valasztas
        valasztas = ""
    return valasztas


def opcio_valasztas_oldal(dontes_leiras: str, opcio_lista: list[int]) -> int:
    valasztas: int = 0
    print(dontes_leiras)
    if len(opcio_lista) == 0:
        return valasztas
    if len(opcio_lista) == 1:
        return opcio_lista[0]

    while valasztas == 0:
        valasztas = int(input(f"Válassz: {opcio_lista}"))
        for valasz_lehetoseg in opcio_lista:
            if valasztas == valasz_lehetoseg:
                return valasztas
        valasztas = 0
    return valasztas
