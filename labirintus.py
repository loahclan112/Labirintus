import random

from karakter import Karakter
from oldal import Oldal

def labirintus_generalasa() -> list[Oldal]:
    oldal_1: Oldal = Oldal(1, [270, 66], "Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették. Ha ki akarod nyitni a dobozt, lapozz a 270-re. Ha inkább tovább haladsz észak felé, lapozz a 66-ra.")
    oldal_56: Oldal = Oldal(56, [373, 215], "Látod, hogy az akadály egy széles, barna, sziklaszerű tárgy. Megérinted, és meglepve tapasztalod, hogy lágy, szivacsszerű. Ha át szeretnél mászni rajta, lapozz a 373-ra. Ha ketté akarod vágni a kardoddal, lapozz a 215-re.")
    oldal_66: Oldal = Oldal(66, [293, 56], "Néhány perc gyaloglás után egy elágazáshoz érsz az alagútban. Egy, a falra festett fehér nyíl nyugatfelé mutat. A földön nedves lábnyomok jelzik, merre haladtak az előtted járók. Nehéz biztosan megmondani, de úgy tűnik, hogy három közülük a nyíl irányába halad, míg egyikük úgy döntött, hogy keletnek megy. Ha nyugat felé kívánsz menni, lapozz a 293-ra. Ha keletnek, lapozz a 56-re")
    oldal_137: Oldal = Oldal(137, [], "Ahogy végigmész az alagúton, csodálkozva látod, hogy egy jókora vasharang csüng alá a boltozatról.")
    oldal_215: Oldal = Oldal(215, [], "Kardod könnyedén áthatol a spóragolyó vékonykülső burkán. Sűrű barna spórafelhő csap ki a golyóból, és körülvesz. Némelyik spóra a bőrödhöz tapad, és rettenetes viszketést okoz. Nagy daganatok nőnek az arcodon és karodon, és a bőröd mintha égne. 2 ÉLETERŐ pontot veszítesz. Vadul vakarózva átléped a leeresztett golyót, és keletnek veszed az utad.")
    oldal_270: Oldal = Oldal(270, [66], "A doboz teteje könnyedén nyílik. Benne két aranypénzt találsz, és egy üzenetet, amely egy kis pergamenen neked szól. Előbb zsebre vágod az aranyakat, aztán elolvasod az üzenetet: - „Jól tetted. Legalább volt annyi eszed, hogy megállj és elfogadd az ajándékot. Most azt tanácsolom neked, hogy keress és használj különféle tárgyakat, ha sikerrel akarsz áthaladni Halállabirintusomon.” Az aláírás Szukumvit. Megjegyzed a tanácsot, apró darabokra téped a pergament, és tovább mész észak felé. Lapozz a 66-ra.")
    oldal_293: Oldal = Oldal(293, [137, 387], "A három pár nedves lábnyomot követve az alagút nyugati elágazásában hamarosan egy újabb el-ágazáshoz érsz. Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re. Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re.")
    oldal_373: Oldal = Oldal(373, [], "Fölmászol a lágy sziklára, attól tartasz, hogy bár-melyik pillanatban elnyelhet. Nehéz átvergődni rajta, mert puha anyagában alig tudod a lábadat emelni, de végül átvergődsz rajta. Megkönnyebbülten érsz újra szilárd talajra, és fordulsz kelet felé.")
    oldal_387: Oldal = Oldal(387, [], "Hallod, hogy elölről súlyos lépések közelednek. Egy széles, állatbőrökbe öltözött, kőbaltás, primitív lény lép elő. Ahogy meglát, morog, a földre köp, majd a kőbaltát felemelve közeledik, és mindennek kinéz, csak barátságosnak nem. Előhúzod kardodat, és felkészülsz, hogy megküzdj a Barlangi Emberrel.")

    labirintus: list[Oldal] = [
        oldal_1,
        oldal_56,
        oldal_66,
        oldal_137,
        oldal_215,
        oldal_270,
        oldal_293,
        oldal_373,
        oldal_387
    ]

    return labirintus

def oldal_keresese(labirintus: list[Oldal], oldalszam: int):
    for oldal in labirintus:
        if oldal.oldalszam == oldalszam:
            return oldal
    return "nincs ilyen oldal"

def jatek(labirintus: list[Oldal], jatekos: Karakter):
    aktiv_oldal: Oldal = labirintus[0]
    kovetkezo_oldal: int = -1
    while kovetkezo_oldal != 0:
        kovetkezo_oldal = aktiv_oldal.esemeny(jatekos)
        if kovetkezo_oldal != 0:
            aktiv_oldal = oldal_keresese(labirintus, kovetkezo_oldal)
    print(f"Véget ért a kalandod!!! Tulajdonságaid: {jatekos}")

def karakter_generalasa() -> Karakter:
    ugyesseg: int = 6 + random.randint(1, 6)
    eletero: int = 12 + random.randint(1, 6) + random.randint(1, 6)
    szerencse: int = random.randint(1, 6)
    jatekos: Karakter = Karakter("játékos", ugyesseg, eletero, szerencse)
    return jatekos