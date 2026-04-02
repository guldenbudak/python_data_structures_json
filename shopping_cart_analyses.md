# Ödev 1 — Alışveriş Sepeti Analizi (liste + dict + for + if)

## Amaç
- Liste içinde gezinme (`for`)
- Koşula göre indirim uygulama (`if`)
- Kategori bazında özet çıkarma (`dict`)
- Edge-case düşünme (hizmete indirim yok, qty >= 3 indirimi, doğru toplamlar)

## Girdi Dosyası
- Dosya: `inputs/odev1_cart.json`
- Format: JSON listesi (her eleman bir ürün satırı)

Her satır şu alanları içerir:
- `name` (str): ürün adı  
- `price` (int/float): birim fiyat  
- `qty` (int): adet  
- `category` (str): kategori (`giyim`, `market`, `hizmet`, `elektronik`, `kozmetik` gibi)

## Kurallar
1. **Toplam tutar**: tüm satırlar için `price * qty`
2. **İndirim**:
   - Eğer `qty >= 3` ise satır bazında **%10 indirim** uygula
   - Ancak `category == "hizmet"` ise **asla indirim uygulama**
3. **Kategori toplamları**:
   - `{"giyim": X, "market": Y, ...}` şeklinde
   - Bu toplamlar **indirimsiz** tutar üzerinden hesaplanacak
4. **En pahalı tekil ürün**:
   - `price` alanı en yüksek olan satır (adı + fiyatı)
   - Eğer aynı fiyat varsa, ilk gördüğünü seçebilirsin

## İstenen Çıktı
Konsola şu formatta yazdır:
- `Toplam (indirimsiz): ...`
- `Toplam (indirimli): ...`
- `Kategori Toplamları: {...}`
- `En pahalı ürün (tekil): <name> - <price>`

## Beklenen Dosya/Script Davranışı
- JSON dosyasını oku
- Hesaplamaları yap
- Çıktıyı yazdır

## Bonus (Opsiyonel)
- Kategori toplamlarını en yüksekten düşüğe sıralayıp yazdır.
