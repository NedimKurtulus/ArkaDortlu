class BasitKasa:
    def __init__(self):
        self.urunler = {}  # {urun_kodu: [isim, fiyat, stok]}
        self.bakiye = 0
        self.satislar = []
    
    def urun_ekle(self, kod, isim, fiyat, stok):
        """Yeni ürün ekler"""
        self.urunler[kod] = [isim, fiyat, stok]
        print(f"{isim} eklendi.")
    
    def satis_yap(self, kod, adet):
        """Satış işlemi yapar"""
        if kod not in self.urunler:
            print("Ürün bulunamadı!")
            return
            
        if self.urunler[kod][2] < adet:
            print("Yetersiz stok!")
            return
            
        # Satış detayları
        isim = self.urunler[kod][0]
        fiyat = self.urunler[kod][1]
        tutar = fiyat * adet
        
        # Stok güncelleme
        self.urunler[kod][2] -= adet
        
        # Bakiye güncelleme
        self.bakiye += tutar
        
        # Satış kaydı
        self.satislar.append([kod, adet, tutar])
        
        # Fiş yazdırma
        print(f"\n--- FİŞ ---")
        print(f"Ürün: {isim}")
        print(f"Adet: {adet}")
        print(f"Fiyat: {fiyat} TL")
        print(f"Toplam: {tutar} TL")
        print("----------")
    
    def rapor_al(self):
        """Basit rapor gösterir"""
        print("\n--- RAPOR ---")
        print(f"Toplam Satış: {len(self.satislar)}")
        print(f"Kasa Bakiye: {self.bakiye} TL")
        print(f"Stok Durumu:")
        for kod, bilgi in self.urunler.items():
            print(f"  {bilgi[0]}: {bilgi[2]} adet")
        print("------------")



# Rapor alma
kasa.rapor_al()

