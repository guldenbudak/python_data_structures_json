# Ödev 4 — Envanter & Sipariş Güncelleme (dict + liste + if)

## Amaç
- Dict içindeki stok bilgisini siparişlere göre güncellemek
- Hatalı senaryoları raporlamak (unknown sku / out of stock / insufficient)
- Gün sonu özet çıkarmak

## Girdi Dosyaları
- Envanter: `inputs/odev4_inventory.json` (dict)
- Siparişler: `inputs/odev4_orders.json` (list)

### Envanter Formatı
```json
{
  "SKU123": {"name": "...", "stock": 10, "price": 500},
  ...
}
```

### Sipariş Formatı
```json
[
  {"order_id": "ORD1000", "sku": "SKU123", "qty": 2},
  ...
]
```

## Kurallar
Bir sipariş işlenirken:
1. SKU envanterde yoksa → `unknown_skus` listesine ekle (order_id, sku)
2. SKU varsa ama stock == 0 → `out_of_stock` listesine ekle
3. Stock < qty ise → `insufficient_stock` listesine ekle
4. Aksi halde:
   - Stoktan düş
   - Sipariş cirosunu ekle: `price * qty`
   - `successful_orders` listesine ekle

## İstenenler
- Gün sonu:
  - Toplam ciro
  - Başarılı sipariş sayısı
  - Sorunlu sipariş raporu (3 liste)
  - Güncellenmiş envanter (stoklar düşmüş hali)
- `low_stock`: stok `<= 2` olan SKU’lar

## Çıktı Formatı (örnek)
- `Revenue: ...`
- `Successful orders: ...`
- `Unknown SKUs: ...`
- `Out of stock: ...`
- `Insufficient stock: ...`
- `Low stock: ...`
- `Updated inventory: ...` (ister yazdır ister json olarak dosyaya yaz)

## Bonus (Opsiyonel)
- Güncellenmiş envanteri `outputs/odev4_inventory_updated.json` olarak kaydet.
