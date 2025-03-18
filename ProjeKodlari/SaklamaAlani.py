from abc import ABC, abstractmethod

# Saklama alanı için arayüz (interface)
class ISaklamaAlani(ABC):
    @abstractmethod
    def sicaklik_guncelle(self, yeni_sicaklik: float):
        pass

    @abstractmethod
    def nem_guncelle(self, yeni_nem: float):
        pass

    @abstractmethod
    def doluluk_guncelle(self, yeni_doluluk: float):
        pass

    @abstractmethod
    def durum_raporu(self):
        pass

# Saklama alanı sınıfı
class SaklamaAlani(ISaklamaAlani):
    def __init__(self, sicaklik: float, nem: float, doluluk: float):
        self.sicaklik = sicaklik  # °C
        self.nem = nem  # %
        self.doluluk = doluluk  # %
    
    def sicaklik_guncelle(self, yeni_sicaklik: float):
        self.sicaklik = yeni_sicaklik
        print(f"Sıcaklık güncellendi: {self.sicaklik}°C")
    
    def nem_guncelle(self, yeni_nem: float):
        self.nem = yeni_nem
        print(f"Nem güncellendi: %{self.nem}")
    
    def doluluk_guncelle(self, yeni_doluluk: float):
        self.doluluk = yeni_doluluk
        print(f"Doluluk oranı güncellendi: %{self.doluluk}")
    
    def durum_raporu(self):
        rapor = f"""
        ** Saklama Alanı Durum Raporu **
        Sıcaklık: {self.sicaklik}°C
        Nem: %{self.nem}
        Doluluk Oranı: %{self.doluluk}
        """
        return rapor


