
from abc import ABC, abstractmethod

# Ürün arayüzü
class IUrun(ABC):
    @abstractmethod
    def fiyat_hesapla(self, miktar):
        pass

# Ürün sınıfı
class Urun(IUrun):
    def __init__(self, ad, birim_fiyat, birim):
        self.ad = ad
        self.birim_fiyat = birim_fiyat
        self.birim = birim

    def fiyat_hesapla(self, miktar):
        if self.birim == "kg":
            return self.birim_fiyat * miktar
        elif self.birim == "adet":
            return self.birim_fiyat * miktar
        else:
            raise ValueError("Geçersiz birim")

# Tartılan ürün sınıfı
class TartilanUrun(Urun):
    def __init__(self, ad, birim_fiyat):
        super().__init__(ad, birim_fiyat, "kg")

# Adetle satılan ürün sınıfı
class AdetleSatilanUrun(Urun):
    def __init__(self, ad, birim_fiyat):
        super().__init__(ad, birim_fiyat, "adet")

# Tartım sınıfı
class Tartim:
    def tart(self, urun, miktar):
        if urun.birim == "kg":
            return miktar
        else:
            raise ValueError("Bu ürün tartılarak satılmaz")

# Adet hesaplama sınıfı
class AdetHesaplama:
    def hesapla(self, urun, adet):
        if urun.birim == "adet":
            return adet
        else:
            raise ValueError("Bu ürün adetle satılmaz")

# Fiyat hesaplama sınıfı
class FiyatHesaplama:
    def hesapla(self, urun, miktar):
        return urun.fiyat_hesapla(miktar)

# Örnek kullanım
kek = TartilanUrun("Kek", 25)
kurabiye = AdetleSatilanUrun("Kurabiye", 2)

tartim = Tartim()
adet_hesaplama = AdetHesaplama()
fiyat_hesaplama = FiyatHesaplama()

tartilan_miktar = tartim.tart(kek, 0.5)
adet = adet_hesaplama.hesapla(kurabiye, 10)

kek_fiyat = fiyat_hesaplama.hesapla(kek, tartilan_miktar)
kurabiye_fiyat = fiyat_hesaplama.hesapla(kurabiye, adet)

print(f"{kek.ad} (0.5 kg): {kek_fiyat} TL")
print(f"{kurabiye.ad} (10 adet): {kurabiye_fiyat} TL")
