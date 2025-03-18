from abc import ABC, abstractmethod

# Personel için arayüz (interface)
class IPersonel(ABC):
    @abstractmethod
    def gorev_bilgisi(self):
        pass
    
    @abstractmethod
    def maas_hesapla(self):
        pass

# Personel sınıfı (Genel)
class Personel(IPersonel):
    def __init__(self, ad, soyad, pozisyon, maas, izin_gunleri):
        self.ad = ad
        self.soyad = soyad
        self.pozisyon = pozisyon
        self.maas = maas
        self.izin_gunleri = izin_gunleri  # Örneğin: ["2025-03-20", "2025-03-21"]
        self.nobet_cizelgesi = []  # Örneğin: ["2025-03-18 Gece", "2025-03-19 Gündüz"]

    def gorev_bilgisi(self):
        return f"{self.ad} {self.soyad} - {self.pozisyon}"

    def maas_hesapla(self):
        return f"{self.ad} {self.soyad} maaşı: {self.maas} TL"

    def izin_ekle(self, tarih):
        self.izin_gunleri.append(tarih)
        return f"{self.ad} {self.soyad} için {tarih} izne eklendi."

    def nobet_ekle(self, tarih, vardiya):
        self.nobet_cizelgesi.append(f"{tarih} {vardiya}")
        return f"{self.ad} {self.soyad} için {tarih} {vardiya} nöbet eklendi."

    def izin_listesi(self):
        return f"{self.ad} {self.soyad} izin günleri: {', '.join(self.izin_gunleri)}"

    def nobet_listesi(self):
        return f"{self.ad} {self.soyad} nöbet çizelgesi: {', '.join(self.nobet_cizelgesi)}"

# Alt sınıflar (Müşteri Destek, Reyon Bakımı, Stok İşlemleri)
class MusteriDestekPersoneli(Personel):
    def __init__(self, ad, soyad, maas, izin_gunleri):
        super().__init__(ad, soyad, "Müşteri Destek", maas, izin_gunleri)

class ReyonBakimPersoneli(Personel):
    def __init__(self, ad, soyad, maas, izin_gunleri):
        super().__init__(ad, soyad, "Reyon Bakımı", maas, izin_gunleri)

class StokPersoneli(Personel):
    def __init__(self, ad, soyad, maas, izin_gunleri):
        super().__init__(ad, soyad, "Stok İşlemleri", maas, izin_gunleri)

