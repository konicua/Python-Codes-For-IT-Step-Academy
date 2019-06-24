class Magazia:
    def __init__(nivtebi, saxeli, fasi):
        nivtebi.saxeli = saxeli
        nivtebi.fasi= fasi

    def getinfo(nivtebi):
        print(nivtebi.saxeli, nivtebi.fasi)

pepsi = Magazia("Pepsi", 0.90)
cocacola = Magazia("Cocacola", 1.10)
dorito = Magazia("Dorito", 1.20)
twix = Magazia("Twix", 1.20)
sprite = Magazia("Sprite", 1.30)
lays = Magazia("Lays", 1.50)
pepper = Magazia("Pepper", 1.55)
chocopie = Magazia("Chocopie", 1.50)
doubletwix = Magazia("DoubleTwix", 1.70)
powder = Magazia("Powder", 2.20)
rice = Magazia("Rice", 2.50)

Magaziis = [pepsi, cocacola, dorito, twix, sprite, lays, pepper, chocopie, doubletwix, powder, rice]

for nivtebi in Magaziis:
    if input(nivtebi.saxeli and nivtebi.fasi):
        nivtebi.getinfo()