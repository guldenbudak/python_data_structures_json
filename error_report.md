# Ödev 2 — Loglardan Hata Raporu (dict + for + if)

## Amaç
- Kayıtları sayma (counter mantığı)
- Servis bazlı hata özetleri
- Gruplama ve raporlama

## Girdi Dosyası
- Dosya: `inputs/odev2_logs.json`
- Format: JSON listesi

Alanlar:
- `ts` (str): ISO tarih/saat
- `level` (str): `INFO` / `WARN` / `ERROR`
- `service` (str): servis adı (örn: auth, payment, order...)
- `msg` (str): mesaj
- `code` (int|null): hata kodu (ERROR dışındakilerde null olabilir)

## İstenenler
1. **Level counts**: level bazında kaç kayıt var?
   - Örn: `{"INFO": 120, "WARN": 50, "ERROR": 53}`
2. **ERROR by service**: sadece `level == "ERROR"` olanları servis bazında say
   - Örn: `{"auth": 12, "payment": 8, ...}`
3. **En çok ERROR üreten servis**
4. **ERROR mesajlarını servislere göre grupla**
   - Örn: `{"auth": ["invalid password", "token expired"], "payment": ["timeout"]}`
   - Aynı mesaj tekrar ediyorsa tekrar ekleyebilirsin **veya** unique yapabilirsin (seçim senin, ama kararını yorum satırıyla belirt)
5. **Alert kuralı**
   - Eğer bir servisin ERROR sayısı `>= 2` ise o servis `ALERT` listesine girsin

## Çıktı Formatı
- `Level counts: {...}`
- `Error by service: {...}`
- `Top error service: <service_name> (<count>)`
- `Alerts: [ ... ]`

## Bonus (Opsiyonel)
- ERROR code dağılımı çıkar: `{"401": 10, "500": 3, ...}`
