import random


class Karakter:
    def __init__(self, nev: str, ugyesseg: int, eletero: int, szerencse: int):
        self.nev = nev
        self.ugyesseg = ugyesseg
        self.eletero = eletero
        self.szerencse = szerencse

    def __str__(self):
        return f"Név: {self.nev} Életerő: {self.eletero} Ügyesség: {self.ugyesseg} Szerencse: {self.szerencse}"
    def tamado_ero(self) -> int:
        kocka_1: int = random.randint(1, 6)
        kocka_2: int = random.randint(1, 6)
        tamado_ero: int = self.ugyesseg + kocka_1 + kocka_2
        print(f"{self.nev} támadó ereje: {tamado_ero} (ügyesség: {self.ugyesseg} + kocka: {kocka_1}+{kocka_2})")
        return tamado_ero

    def szerencse_proba(self) -> bool:
        kocka_1: int = random.randint(1, 6)
        kocka_2: int = random.randint(1, 6)
        self.szerencse -= 1
        szerencse: bool = kocka_1 + kocka_2 < self.szerencse
        if(szerencse):
            print( f"{self.nev} Szerencsés volt! (szerencse: {self.szerencse} > kocka: {kocka_1}+{kocka_2})")
        else:
            print( f"{self.nev} Balszerencsés volt! (szerencse: {self.szerencse} < kocka: {kocka_1}+{kocka_2})")

        return szerencse

    def el_e(self) -> bool:
        return self.eletero > 0
