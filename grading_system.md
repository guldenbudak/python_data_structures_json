# Ödev 3 — Öğrenci Not Sistemi (liste/dict + if/for)

## Amaç
- Liste içindeki sayıları işleyip ortalama hesaplama
- Koşullara göre harf notu verme
- Özet istatistik çıkarma

## Girdi Dosyası
- Dosya: `inputs/odev3_students.json`
- Format: JSON listesi

Alanlar:
- `name` (str)
- `scores` (list[int]): 3-6 arası not

## Notlandırma Kuralları
Ortalama:
- `>= 85` → `"AA"`
- `70-84.999...` → `"BB"`
- `50-69.999...` → `"CC"`
- `< 50` → `"FF"`

## İstenenler
1. Her öğrenci için ortalama hesapla
2. Harf notunu belirle
3. Şu formatta `results` listesi üret:
   ```python
   results = [
     {"name": "Ayşe", "avg": 80.0, "grade": "BB"},
     ...
   ]
   ```
4. Sınıf ortalaması
5. En yüksek ve en düşük ortalamalı öğrenciler (ad + ortalama)
6. `FF` olanları ayrı listeye koy: `failed_students`

## Çıktı
- Her öğrenciyi tek satır yazdır: `Ayşe -> avg: 80.00, grade: BB`
- Sonda:
  - `Class average: ...`
  - `Top student: ...`
  - `Bottom student: ...`
  - `Failed: [ ... ]`

## Bonus (Opsiyonel)
- Harf notlarına göre dağılım: `{"AA": 3, "BB": 5, ...}`
