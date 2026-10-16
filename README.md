# Üniversite kapısında kadınlar erkekleri ne zaman geçti?

Yükseköğretimde kadın ve erkek okullaşmasının yarım yüzyıllık hikâyesi ve Türkiye'nin bu hikâyedeki yeri. Kaydırdıkça değişen interaktif bir veri hikâyesi (scrollytelling).

**Canlı site:** [SİTE BAĞLANTISI]
**Yazar:** Kübra Önaybırak

## Çalışma sorusu
Kadınlar yükseköğretimde erkekleri hangi ülkelerde ve ne zaman geride bıraktı; Türkiye bu hikâyenin neresinde?

## Ana bulgular
- 1971'de verisi olan ülkelerin yalnızca %11'inde kadınlar önde; 2024'te %87.
- Bu pay 2001'de ilk kez %50'yi aştı.
- Türkiye'de kadınlar 2021'den beri erkeklerin önünde.

## Veri kaynağı ve lisans
Dünya Bankası Açık Veri: brüt yükseköğretim okullaşma oranı, kadın (SE.TER.ENRR.FE) ve erkek (SE.TER.ENRR.MA). Lisans: CC BY 4.0. Erişim tarihi: 16 Ekim 2026. Ham dosyalar `data/raw/` içinde, sitede kullanılan özet dosya `data/processed/gap.csv` (4.589 satır, 203 ülke, 1970–2025).

## Klasör yapısı
```
data/raw/        ham Dünya Bankası dosyaları
data/processed/  sitede kullanılan özet veri (gap.csv)
notebooks/       analiz.ipynb (ve aynı kodun analiz.py sürümü)
site/            index.html, og.png, data/gap.csv
docs/            storyboard.pdf, tasarim_notu.pdf
```

## Yerelde çalıştırma
1. `pip install pandas jupyter`
2. `notebooks/analiz.ipynb` dosyasını açıp "Restart & Run All" yapın. Bu işlem `data/processed/gap.csv` ve `site/data/gap.csv` dosyalarını üretir.
3. `site/` klasöründe `python -m http.server` çalıştırıp `http://localhost:8000` adresini açın.

Sitedeki `index.html` veriyi önce `data/gap.csv` dosyasından okur; dosya bulunamazsa aynı verinin sayfaya gömülü kopyasına geçer. Böylece site çift tıklanarak da açılabilir.

## Kullanılan kütüphaneler ve kod kaynakları
Analiz: Python, pandas. Site: saf HTML, CSS, JavaScript ve SVG; kaydırma adımları Intersection Observer API ile yönetilir. Üçüncü taraf kod veya şablon kullanılmadı.

## Yapay zekâ kullanım beyanı
Claude (Anthropic), kod yazımı ve hata ayıklama için kullanıldı (ör. siteyi veri dosyası olmadan da çalışır hâle getirme, notebook düzeltmeleri). Analiz yorumları ve hikâye metni yazara aittir.
