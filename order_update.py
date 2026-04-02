import json

with open('/Users/gulden/Downloads/python_odevleri (1)/inputs/odev4_inventory.json') as file:
    inventory = json.load(file)
with open('/Users/gulden/Downloads/python_odevleri (1)/inputs/odev4_orders.json') as file:
    orders = json.load(file)

unknown_skus = []
out_of_stock = []
insufficient_stock = []
successful_orders = []
revenue = []
low_stock = []
update_inventory = {}
for key, value in inventory.items():
    inventory.keys()

    for order in orders:
        order_id = order['order_id']
        sku = order['sku']
        qty = order['qty']

        if order['sku'] in inventory:

            if value['stock'] == 0:
                out_of_stock.append(f"order_id: {order_id}, sku: {sku}")

            if value['stock'] < qty:
                insufficient_stock.append(f"order_id: {order_id}, sku: {sku}")

            if value['stock'] <= 2:
                low_stock.append(f"order_id: {order_id}, sku: {sku}")

            else:
                value['stock'] -= 1
                endorsement = value['price'] * qty
                successful_orders.append(f"order_id: {order_id}, endorsement: {endorsement}")
                update_inventory[order_id] = value

        elif order['sku'] not in inventory:
            unknown_skus.append(f"order_id: {order_id}, sku: {sku}")

print(f"out_of_stock: {out_of_stock}")
print(f"insufficient_stock: {insufficient_stock}")
print(f"successful_orders: {len(successful_orders)}")
print(f"unknown_skus: {unknown_skus}")
print(f"low_stock: {low_stock}")

top_endorsements = 0
for key, value in inventory.items():
    inventory.keys()

    for order in orders:
        order_id = order['order_id']
        sku = order['sku']
        qty = order['qty']

        for item in successful_orders:
            endorsement = value['price'] * qty
            top_endorsements += endorsement
            revenue.append(f"top_endorsements: {top_endorsements}")

print(f"top_endorsements: {top_endorsements}")

with open('json_data.json', 'w') as fp:
    json.dump(update_inventory, fp)