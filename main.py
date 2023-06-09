from insan import İnsan
from issiz import İşsiz
from calisan import Çalişan
from maviyaka import MaviYaka
from beyazyaka import BeyazYaka
import pandas as pd

insan1 = İnsan(72156070558, "mücadiye", "dayanir", 35, "kadin", "arnavut")
insan2 = İnsan(81578421848, "berkecan", "çebi", 28, "erkek", "türk")

işsiz1 = İşsiz(13356975076, "didar", "kurtuldu", 22, "kadin", "avusturyali", 1, 4, 2)
işsiz2 = İşsiz(62738570378, "doğaç", "tiraş",  23, "erkek", "afgan", 0, 0, 5)
işsiz3 = İşsiz(14650561446, "selçuk", "ertem", 18, "erkek", "belçikali", 2, 4, 0)
işsiz1.__str__()
işsiz2.__str__()
işsiz3.__str__()

çalişan1 = Çalişan(48588356232, "boğaçhan", "uluba", 25, "erkek", "çek", "enerji", 22, 16500)
çalişan2 = Çalişan(56733636818, "eliz", "özhan", 26, "kadin", "ingiliz", "inşaat", 21, 12000)
çalişan3 = Çalişan(24014683288, "mahmut emre", "çolakoğlu", 17, "erkek", "misirli", "medya, iletişim ve yayincilik", 19, 19275)
çalişan1.__str__()
çalişan2.__str__()
çalişan3.__str__()

maviyaka1 = MaviYaka(17214745382, "nafize", "bağdatli", 21, "kadin", "fransali", "otomativ", 25, 11895, 0.8)
maviyaka2 = MaviYaka(23804070970, "şule", "ayaz", 29, "kadin", "hollandali", "kültür, sanat ve tasarim", 49, 9800, 0.4)
maviyaka3 = MaviYaka(44327457376, "savaş", "ilkay", 33, "erkek", "macar", "elektrik ve elektronik", 18, 15900, 0.3)
maviyaka1.__str__()
maviyaka2.__str__()
maviyaka3.__str__()

beyazyaka1 = BeyazYaka(34181147278, "kenan", "özder", 47, "erkek", "hintli", "metal", 39, 22000, 2000)
beyazyaka2 = BeyazYaka(40321944164, "şeyma", "kumbul", 15, "kadin", "iranli", "spor ve rekreasyon", 33, 35600, 1500)
beyazyaka3 = BeyazYaka(89609239578, "zafer", "dizbay", 27, "erkek", "italyan", "ticaret", 50, 18540, 500)
beyazyaka1.__str__()
beyazyaka2.__str__()
beyazyaka3.__str__()
liste = {
    "nesne değeri": ["çalişan", "çalişan", "çalişan", "mavi yaka", "mavi yaka", "mavi yaka", "beyaz yaka", "beyaz yaka", "beyaz yaka"],
    "tc no": [çalişan1.get_tc_no(), çalişan2.get_tc_no(), çalişan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
    "ad": [çalişan1.get_ad(), çalişan2.get_ad(), çalişan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
    "soyad": [çalişan1.get_soyad(), çalişan2.get_soyad(), çalişan3.get_soyad(), maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
    "yaş": [çalişan1.get_yas(), çalişan2.get_yas(), çalişan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
    "cinsiyet": [çalişan1.get_cinsiyet(), çalişan2.get_cinsiyet(), çalişan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
    "uyruk": [çalişan1.get_uyruk(), çalişan2.get_uyruk(), çalişan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
    "sektör": [çalişan1.get_sektör(), çalişan2.get_sektör(), çalişan3.get_sektör(), maviyaka1.get_sektör(), maviyaka2.get_sektör(), maviyaka3.get_sektör(), beyazyaka1.get_sektör(), beyazyaka2.get_sektör(), beyazyaka3.get_sektör()],
    "tecrübe": [çalişan1.get_tecrübe() / 12, çalişan2.get_tecrübe() / 12, çalişan3.get_tecrübe() / 12, maviyaka1.get_tecrübe() / 12, maviyaka2.get_tecrübe() / 12, maviyaka3.get_tecrübe() / 12, beyazyaka1.get_tecrübe() / 12, beyazyaka2.get_tecrübe() / 12, beyazyaka3.get_tecrübe() / 12],
    "maaş": [çalişan1.get_maaş(), çalişan2.get_maaş(), çalişan3.get_maaş(), maviyaka1.get_maaş(), maviyaka2.get_maaş(), maviyaka3.get_maaş(), beyazyaka1.get_maaş(), beyazyaka2.get_maaş(), beyazyaka3.get_maaş()],
    "yipranma payi": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0, 0, 0],
    "teşvik primi": [0, 0, 0, 0, 0, 0, beyazyaka1.get_teşvik_primi(), beyazyaka2.get_teşvik_primi(), beyazyaka3.get_teşvik_primi()],
    "yeni maaş": [çalişan1.zam_hakki(), çalişan2.zam_hakki(), çalişan3.zam_hakki(), maviyaka1.zam_hakki(), maviyaka2.zam_hakki(), maviyaka3.zam_hakki(), beyazyaka1.zam_hakki(), beyazyaka2.zam_hakki(), beyazyaka3.zam_hakki()]
}
data = pd.DataFrame(liste)
data.fillna(0, inplace=True)
print(f"***   Data Frame   ***\n\n{data}\n")

ortalamalar = data.groupby('nesne değeri')[['tecrübe', 'yeni maaş']].mean()
print(f"*** Tecrübe ve Yeni Maaşlarin Ortalamasi ***\n\n{ortalamalar}\n")

yüksek_maaş_sayisi = data[data["maaş"] > 15000].shape[0]
print(f"Maaşi 15000 TL üzerinde olanlarin sayisi: {yüksek_maaş_sayisi}\n")

sirali_data = data.sort_values(by="yeni maaş")
sirali_liste = sirali_data['yeni maaş'].values.tolist()
print(f"Yeni maaşlarin siralanmiş listesi: {sirali_liste}\n")

beyazyaka_tecrübe = data[(data["nesne değeri"] == "beyaz yaka") & (data["tecrübe"] > 3)]
beyazyaka_tecrübe = beyazyaka_tecrübe[['nesne değeri', 'tecrübe']]
print(f"*** Tecrübesi 3 Yildan Fazla Olan Beyaz Yakalar ***\n\n{beyazyaka_tecrübe}\n")

yeni_maaş_yüksek = data[data["yeni maaş"] > 10000].loc[2:5, ["tc no", "yeni maaş"]]
print(f"*** Yeni Maaşi 10000'den fazla olan 2'den 5'e Kadar Tc ve Yeni Maaşlar ***\n\n{yeni_maaş_yüksek}\n")

yeni_data = data[["ad", "soyad", "sektör", "yeni maaş"]]
print(f"*** Ad, Soyad, Sektör, Yeni Maaş Değerleri ***\n\n{yeni_data}")