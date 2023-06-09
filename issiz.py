from insan import İnsan

class İşsiz(İnsan):
    def __init__(self, tc_adi, ad, soyad, yas, cinsiyet, uyruk, beyaz_yaka, mavi_yaka, yönetici):
        super().__init__(tc_adi, ad, soyad, yas, cinsiyet, uyruk)
        self.__beyaz_yaka = beyaz_yaka
        self.__mavi_yaka = mavi_yaka
        self.__yönetici = yönetici
        self.__statü = ""
        self.__tecrübe = {'beyaz yaka': self.get_beyaz_yaka(), 'mavi yaka': self.get_mavi_yaka(), 'yönetici': self.get_yönetici()}
        self.statu_bul()

    def set_beyaz_yaka(self, beyaz_yaka):
        self.__beyaz_yaka = beyaz_yaka

    def get_beyaz_yaka(self):
        return self.__beyaz_yaka
    
    def set_mavi_yaka(self, mavi_yaka):
        self.__mavi_yaka = mavi_yaka

    def get_mavi_yaka(self):
        return self.__mavi_yaka
    
    def set_yönetici(self, yönetici):
        self.__yönetici = yönetici

    def get_yönetici(self):
        return self.__yönetici
    
    def set_statü(self, statü):
        self.__statü = statü

    def get_statü(self):
        return self.__statü
    
    def statu_bul(self):
        if (float(self.__tecrübe['beyaz yaka']) * 35 / 100 >= float(self.__tecrübe['mavi yaka']) * 20 / 100) and (float(self.__tecrübe['beyaz yaka']) * 35 / 100 >= float(self.__tecrübe['yönetici']) * 45 / 100):
            self.__statü = "beyaz yaka"
        elif (float(self.__tecrübe['mavi yaka']) * 20 / 100 >= float(self.__tecrübe['beyaz yaka']) * 35 / 100) and (float(self.__tecrübe['mavi yaka']) * 20 / 100 >= float(self.__tecrübe['yönetici']) * 45 / 100):
            self.__statü =  "mavi yaka"
        else:
            self.__statü = "yönetici"
        
    def __str__(self):
        super().__str__()
        print(f"statü: {self.get_statü()}\n")