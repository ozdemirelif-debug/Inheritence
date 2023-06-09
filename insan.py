class İnsan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_tc_no(self):
        return self.__tc_no
    
    def set_ad(self, ad):
        self.__ad = ad

    def get_ad(self):
        return self.__ad
    
    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_soyad(self):
        return self.__soyad
    
    def set_yas(self, yas):
        self.__yas = yas

    def get_yas(self):
        return self.__yas
    
    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_cinsiyet(self):
        return self.__cinsiyet
    
    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def get_uyruk(self):
        return self.__uyruk
    
    def __str__(self):
        print(f"\ntc: {self.get_tc_no()}\n\nad: {self.get_ad()}\n\nsoyad: {self.get_soyad()}\n\nyaş: {self.get_yas()}\n\ncinsiyet: {self.get_cinsiyet()}\n\nuyruk: {self.get_uyruk()}\n")
