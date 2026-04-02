import json

with open('../shopping-cart-analyses/inputs/odev1_cart.json', 'r') as file:
    data = json.load(file)

for urun in data:
    category = urun['category']
    name = urun['name']
    price = urun['price']
    qty = urun['qty']
    total = price * qty
    print("Total categories without discount", category, name, qty, total)

for urun in data:
    qty = urun['qty']
    price = urun['price']
    category = urun['category']
    name = urun['name']
    total = price * qty

    if qty >= 3:
        total = total - (total * 10 / 100)
        print("Total categories without discount", category, name, qty, total)
    else:
        print("Without discount ", category, name, qty, total)

hizmet_toplam = 0
market_toplam = 0
kozmetik_toplam = 0
elektronik_toplam = 0
giyim_toplam = 0

for urun in data:
    qty = urun['qty']
    price = urun['price']
    category = urun['category']
    total = price * qty

    if category == 'market':
        market_toplam += total
    elif category == 'kozmetik':
        kozmetik_toplam += total
    elif category == 'elektronik':
        elektronik_toplam += total
    elif category == 'giyim':
        giyim_toplam += total
    elif category == 'hizmet':
        hizmet_toplam += total
print("Market Toplam: ", market_toplam)
print("Kozmetik Toplam: ", kozmetik_toplam)
print("Elektronik Toplam: ", elektronik_toplam)
print("Giyim Toplam: ", giyim_toplam)
print("Hizmet Toplam: ", hizmet_toplam)

priceAlaniEnBuyukMarket = 0
priceAlaniEnBuyukKozmetik = 0
priceAlaniEnBuyukGiyim = 0
priceAlaniEnBuyukElektronik = 0
priceAlaniEnBuyukHizmet = 0

for urun in data:
    category = urun['category']
    name = urun['name']
    price = urun['price']
    if urun['category'] == 'market' and price > priceAlaniEnBuyukMarket:
        priceAlaniEnBuyukMarket = price

    elif urun['category'] == 'kozmetik' and price > priceAlaniEnBuyukKozmetik:
        priceAlaniEnBuyukKozmetik = price

    elif urun['category'] == 'giyim' and price > priceAlaniEnBuyukGiyim:
        priceAlaniEnBuyukGiyim = price

    elif urun['category'] == 'elektronik' and price > priceAlaniEnBuyukElektronik:
        priceAlaniEnBuyukElektronik = price

    elif urun['category'] == 'hizmet' and price > priceAlaniEnBuyukHizmet:
        priceAlaniEnBuyukHizmet = price
    else:
        pass
print("Price alanı en büyük market", priceAlaniEnBuyukMarket)
print("Price alanı en büyük kozmetik", priceAlaniEnBuyukKozmetik)
print("Price alanı en büyük giyim", priceAlaniEnBuyukGiyim)
print("Price alanı en büyük elektron", priceAlaniEnBuyukElektronik)
print("Price alanı en büyük hizmet", priceAlaniEnBuyukHizmet)