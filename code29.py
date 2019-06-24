class Pensionerebi:
    def __init__(pensionerebi, saxeli, gvari, asaki, pensia):
        pensionerebi.saxeli = saxeli
        pensionerebi.gvari = gvari
        pensionerebi.asaki = asaki
        pensionerebi.pensia = pensia

    def getinfo(pensionerebi):
        print(pensionerebi.saxeli, pensionerebi.gvari, pensionerebi.asaki, pensionerebi.pensia)
babu = Pensionerebi("ემზარი", "აბშიძე", 60, 160)
bebo = Pensionerebi("ელო", "ბოტკოველი", 65, 165)
babu1 = Pensionerebi("ნუგზო", "ჭავჭავაძე", 70, 170)
bebo1 = Pensionerebi("კატო", "გაგნიძე", 75, 175)
babu2 = Pensionerebi("უშანგი", "ახალკაცი", 80, 180)
bebo2 = Pensionerebi("მარიჩუნა", "გურგენიძე", 85, 185)
babu3 = Pensionerebi("ალახვერდ", "დალახვერდოვი", 90, 190)
bebo3 = Pensionerebi("კეტონალი", "დეკანოიძე", 95, 195)

Pensionerebis = [babu, bebo, babu1, bebo2, babu3, bebo3]
for pensionerebi in Pensionerebis:
    if pensionerebi.asaki > 85:
        pensionerebi.getinfo()