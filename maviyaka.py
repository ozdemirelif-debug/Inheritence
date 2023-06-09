from calisan import Çalişan

class MaviYaka(Çalişan):
    def __init__(self, tc_adi, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe, maaş, yipranma_payi):
        super().__init__(tc_adi, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe, maaş)
        self.__yipranma_payi = yipranma_payi

    def set_teşvik_primi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
    
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    
    def zam_hakki(self):
        if self.get_tecrübe() < 24:
            self.__yeni_maaş = self.get_maaş() * (100 + self.get_yipranma_payi() * 10) / 100
        elif self.get_tecrübe() >= 24 and self.get_tecrübe() <= 48 and self.get_maaş() < 15000:
            self.__yeni_maaş = self.get_maaş() * (100 + (((self.get_maaş() % self.get_tecrübe())/2) + (self.get_yipranma_payi() * 10)) / 100)
        elif self.get_tecrübe() > 48 and self.get_maaş() < 25000:
            self.__yeni_maaş = self.get_maaş() * (100 + ((self.get_maaş() % self.get_tecrübe()) / 3 + self.get_yipranma_payi() * 10)) / 100
        else:
            self.__yeni_maaş = self.get_maaş()
        return self.__yeni_maaş
    
    def __str__(self):
        super().__str__()
        print(f"yeni maaş: {self.zam_hakki()}\n\nyipranma payi: {self.get_yipranma_payi()}\n")