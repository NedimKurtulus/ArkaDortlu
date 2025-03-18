from abc import ABC, abstractmethod

# Mali işlemler için bir arayüz (interface)
class IMaliModul(ABC):
    @abstractmethod
    def harcama_ekle(self, miktar, kategori, aciklama):
        pass

    @abstractmethod
    def gelir_ekle(self, miktar, aciklama):
        pass

    @abstractmethod
    def kar_zarar_hesapla(self):
        pass

    @abstractmethod
    def mali_rapor(self):
        pass

# Mali Modül Sınıfı
class MaliModul(IMaliModul):
    def __init__(self):
        self.harcamalar = []  # Harcama listesi (tarih, miktar, kategori, açıklama)
        self.gelirler = []  # Gelir listesi (tarih, miktar, açıklama)

    def harcama_ekle(self, miktar, kategori, aciklama):
        self.harcamalar.append({"miktar": miktar, "kategori": kategori, "aciklama": aciklama})
        print(f"Harcama eklendi: {miktar} TL - {kategori} ({aciklama})")

    def gelir_ekle(self, miktar, aciklama):
        self.gelirler.append({"miktar": miktar, "aciklama": aciklama})
        print(f"Gelir eklendi: {miktar} TL - {aciklama}")

    def kar_zarar_hesapla(self):
        toplam_gelir = sum(g["miktar"] for g in self.gelirler)
        toplam_gider = sum(h["miktar"] for h in self.harcamalar)
        kar_zarar = toplam_gelir - toplam_gider
        return toplam_gelir, toplam_gider, kar_zarar

    def mali_rapor(self):
        toplam_gelir, toplam_gider, kar_zarar = self.kar_zarar_hesapla()
        durum = "Kâr" if kar_zarar >= 0 else "Zarar"
        return f"""
       **Mali Durum Raporu**
        Toplam Gelir: {toplam_gelir} TL
        Toplam Gider: {toplam_gider} TL
        Kâr/Zarar Durumu: {kar_zarar} TL ({durum})
        """


