from harcmenet import harc
from karakter import Karakter
from kozos import opcio_valasztas_oldal


class Oldal:
    def __init__(self, oldalszam: int, dontes_oldalszamok: list[int], leiras: str):
        self.oldalszam = oldalszam
        self.dontes_oldalszamok = dontes_oldalszamok
        self.leiras = leiras

    def esemeny(self, jatekos: Karakter) -> int:
        kovetkezo_oldal: int = 0
        if self.oldalszam == 215:
            jatekos.eletero -= 2
        elif self.oldalszam == 387:
            harc(jatekos, Karakter("Barlangi ember", 7, 7, 0))
        else:
            kovetkezo_oldal = opcio_valasztas_oldal(self.leiras, self.dontes_oldalszamok)

        return kovetkezo_oldal
