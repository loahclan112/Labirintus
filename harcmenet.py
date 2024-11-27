from karakter import Karakter
from kozos import opcio_valasztas


def harc(jatekos: Karakter, celpont: Karakter):
    ki_nyert = "senki"

    while ki_nyert == "senki":
        ki_nyert = kor(jatekos, celpont)

    print(f"A(z) {ki_nyert} győzte a csatát!")

def kor(jatekos: Karakter, celpont: Karakter):
    ki_nyert:str = "senki"
    tamado_ero_sajat: int = jatekos.tamado_ero()
    tamado_ero_celpont: int = celpont.tamado_ero()

    if tamado_ero_sajat > tamado_ero_celpont:
        jatekos_sebez(jatekos, celpont)
    elif tamado_ero_sajat < tamado_ero_celpont:
        jatekos_serul(jatekos)
    else:
        print("Kivédtétek egymás csapását!")

    if jatekos.el_e() and not celpont.el_e():
        ki_nyert = jatekos.nev
    elif not jatekos.el_e() and celpont.el_e():
        ki_nyert = celpont.nev

    return ki_nyert

def jatekos_sebez(jatekos: Karakter, celpont: Karakter):
    print(f"{jatekos.nev} Sebez!!")
    sebzes: int = 2
    if jatekos.szerencse > 1:
        valasztas = opcio_valasztas(f"Szeretnél sebzésre használni szerencsepontot? (jelenleg: {jatekos.szerencse}) Ha szerencséd van akkor duplázódik a sebzés, balszerencsénél 1 pont lesz!", ["igen", "nem"])
        if valasztas == "igen":
            sikeres_proba = jatekos.szerencse_proba()
            if sikeres_proba:
                sebzes = 4
            else:
                sebzes = 1
    celpont.eletero -= sebzes
    print(f"{celpont.nev} sérül {sebzes}-t!! Fennmaradó életerő: {celpont.eletero}")


def jatekos_serul(jatekos: Karakter):
    print(f"{jatekos.nev} Sérül!!")
    serules: int = 2
    if jatekos.szerencse > 1:
        valasztas = opcio_valasztas(f"Szeretnél sérülésre használni szerencsepontot? (jelenleg: {jatekos.szerencse}) Ha szerencséd van akkor 1-et sérülsz, balszerencsénél 3-at!", ["igen", "nem"])
        if valasztas == "igen":
            sikeres_proba = jatekos.szerencse_proba()
            if sikeres_proba:
                serules = 1
            else:
                serules = 3
    jatekos.eletero -= serules
    print(f"{jatekos.nev} sérül {serules}-t!! Fennmaradó életerő: {jatekos.eletero}")
