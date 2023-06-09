from calisan import Çalişan

class BeyazYaka(Çalişan):
    def __init__(self, tc_adi, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe, maaş, teşvik_primi):
        super().__init__(tc_adi, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe, maaş)
        self.__teşvik_primi = teşvik_primi

    def set_teşvik_primi(self, teşvik_primi):
        self.__teşvik_primi = teşvik_primi

    def get_teşvik_primi(self):
        return self.__teşvik_primi
    
    def zam_hakki(self):
        if self.get_tecrübe() < 24:
            self.__yeni_maaş = self.get_maaş() * self.get_teşvik_primi() / 100
        elif self.get_tecrübe() >= 24 and self.get_tecrübe() <= 48 and self.get_maaş() < 15000:
            self.__yeni_maaş = self.get_maaş() * ((self.get_maaş() % self.get_tecrübe()) * 5 + self.get_teşvik_primi()) / 100
        elif self.get_tecrübe() > 48 and self.get_maaş() < 25000:
            self.__yeni_maaş = self.get_maaş() * ((self.get_maaş() % self.get_tecrübe()) * 4 + self.get_teşvik_primi()) / 100
        else:
            self.__yeni_maaş = self.get_maaş()
        return self.__yeni_maaş
    def __str__(self):
        super().__str__()
        print(f"yeni maaş: {self.zam_hakki()}\n\nteşvik primi: {self.get_teşvik_primi()}\n")