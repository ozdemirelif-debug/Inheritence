from insan import İnsan

class Çalişan(İnsan):
    def __init__(self, tc_adi, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe, maaş):
        super().__init__(tc_adi, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektör = sektör
        self.__tecrübe = tecrübe
        self.__maaş = maaş
    
    def set_sektör(self, sektör):
        self.__sektör = sektör

    def get_sektör(self):
        return self.__sektör
    
    def set_tecrübe(self, tecrübe):
        self.__tecrübe = tecrübe

    def get_tecrübe(self):
        return self.__tecrübe
    
    def set_maaş(self, maaş):
        self.__maaş = maaş

    def get_maaş(self):
        return self.__maaş
    
    def zam_hakki(self):
        if self.get_tecrübe() < 24:
            self.__yeni_maaş = self.get_maaş()
        elif self.get_tecrübe >= 24 and self.get_tecrübe() <= 48 and self.get_maaş() < 15000:
            self.__yeni_maaş = self.__maaş * (100 + (self.__maaş % self.__tecrübe)) / 100
        elif self.get_tecrübe() > 48 and self.get_maaş() < 25000:
            self.__yeni_maaş = self.__maaş * (100 + ((self.__maaş % self.__tecrübe)/2)) / 100
        else:
            self.__yeni_maaş = self.__maaş
        return self.__yeni_maaş
    
    def __str__(self):
        super().__str__()
        print(f"tecrübe: {self.get_tecrübe()}\n\neski maaş: {self.get_maaş()}\n")
    