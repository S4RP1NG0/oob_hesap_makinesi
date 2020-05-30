class HesapMakinesi():
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def toplama(self):
        toplam = self.sayi1 + self.sayi2
        print("{}+{}= {}".format(self.sayi1,self.sayi2,toplam))

    def cikarma(self):
        cikan = self.sayi1 - self.sayi2
        print("{}-{}= {}".format(self.sayi1,self.sayi2,cikan))

    def carpma(self):
        carpan = self.sayi1 * self.sayi2
        print("{}*{}= {}".format(self.sayi1,self.sayi2,carpan))

    def bolme(self):
        bolen = self.sayi1 / self.sayi2
        print("{}/{}= {}".format(self.sayi1,self.sayi2,bolen))
print("""
S4RP1NG0 Hesap Makinesi
Yapılacak İşlemler :
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
Programdan çıkmak için "x" e Basınız.""")

işlem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz :")
if (işlem == "x"):
    print("Programdan Çıkılıyor...")
    exit()
sayi1 = int(input("Birinci Sayı: "))
sayi2 = int(input("İkinci Sayı: "))
sonuc = HesapMakinesi(sayi1,sayi2)

if (işlem == "1"):
    sonuc.toplama()   
elif (işlem == "2"):
    sonuc.cikarma()
elif (işlem == "3"):
    sonuc.carpma() 
elif (işlem == "4"):
    sonuc.bolme()
