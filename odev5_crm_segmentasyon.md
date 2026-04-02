# Ödev 5 — Mini CRM Segmentasyonu (liste + dict + for + if)

## Amaç
- Müşteri siparişlerinden metrik çıkarmak
- Segment kuralları uygulamak
- Segment bazında özet üretmek

## Girdi Dosyası
- Dosya: `inputs/odev5_customers.json`
- Format: JSON listesi

Alanlar:
- `id` (int)
- `name` (str)
- `orders` (list[int]): sipariş tutarları (boş olabilir)

## Hesaplanacak Metrikler
Her müşteri için:
- `order_count` = len(orders)
- `total_spend` = sum(orders)
- `avg_basket` = total_spend / order_count (order_count == 0 ise 0)

## Segment Kuralları
- `total_spend >= 3000` → `"VIP"`
- değilse `order_count >= 3` → `"Loyal"`
- değilse `order_count == 0` → `"New"`
- diğer → `"Regular"`

## İstenenler
1. `customers_segmented` listesi üret:
   ```python
   {"id": 1, "name": "...", "order_count": 3, "total_spend": 1950, "avg_basket": 650.0, "segment": "Loyal"}
   ```
2. Segment bazında müşteri sayısı (`segment_counts`)
3. En yüksek toplam harcaması olan müşteri
4. **Upsell önerisi listesi**:
   - Segmenti VIP olmayan ama `order_count >= 3` olan müşteriler

## Çıktı Formatı
- Her müşteri için tek satır: `Name (id) -> segment, total_spend, order_count, avg_basket`
- Sonda:
  - `Segment counts: {...}`
  - `Top spender: ...`
  - `Upsell candidates: [ ... ]`

## Bonus (Opsiyonel)
- `customers_segmented` çıktısını `outputs/odev5_customers_segmented.json` olarak kaydet.
