
DOSYA_ADI = "stok_kayitlari.txt"

# Günlük stok giriş/çıkış kaydı
def stok_kaydet(tarih, urun, miktar, islem_tipi):
    with open(DOSYA_ADI, "a", encoding="utf-8") as dosya:
        dosya.write(f"{tarih} | {urun} | {miktar} | {islem_tipi}\n")

# Haftalık stok özetini göster
def haftalik_ozet():
    if not os.path.exists(DOSYA_ADI):
        print("Henüz kayıt yok.")
        return
    
    stoklar = {}
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()
        
        for satir in satirlar:
            tarih, urun, miktar, islem_tipi = satir.strip().split(" | ")
            miktar = int(miktar)
            if urun not in stoklar:
                stoklar[urun] = 0
            if islem_tipi == "Giriş":
                stoklar[urun] += miktar
            elif islem_tipi == "Çıkış":
                stoklar[urun] -= miktar
    
    print("\nHaftalık Stok Özeti:")
    for urun, miktar in stoklar.items():
        print(f"{urun}: {miktar} adet")

# Ana program
def main():
    while True:
        print("\nStok Takip Sistemi")
        print("1. Stok Girişi")
        print("2. Stok Çıkışı")
        print("3. Haftalık Özet")
        print("4. Çıkış")
        
        secim = input("Seçiminiz (1-4): ")
        
        if secim == "4":
            print("Programdan çıkılıyor...")
            break
        
        if secim in ["1", "2"]:
            urun = input("Ürün adını girin: ")
            try:
                miktar = int(input("Miktarı girin: "))
                if miktar < 0:
                    print("Miktar negatif olamaz!")
                    continue
            except ValueError:
                print("Geçerli bir sayı girin!")
                continue
            
            tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            islem_tipi = "Giriş" if secim == "1" else "Çıkış"
            stok_kaydet(tarih, urun, miktar, islem_tipi)
            print(f"{islem_tipi} işlemi kaydedildi: {miktar} adet {urun}")
        
        elif secim == "3":
            haftalik_ozet()
        
        else:
            print("Geçersiz seçim, lütfen 1-4 arasında bir sayı girin.")

# Programı başlat
if __name__ == "__main__":
    main()
