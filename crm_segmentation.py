import json

with open('/Users/gulden/Downloads/python_odevleri (1)/inputs/odev5_customers.json') as file:
    customers = json.load(file)

customer_segmented = []
users = {}
segment_count = {}
highest = 0
top_spender = ""
upsell_candidates = []
for customer in customers:
    id = customer['id']
    name = customer['name']
    orders = customer['orders']
    order_count = len(orders)
    total_spend = sum(orders)

    if order_count == 0:
        avg_basket = 0
    else:
        avg_basket = total_spend / order_count

    if total_spend >= 3000:
        segment = "VIP"

    elif order_count >= 3:
        segment = "Loyal"

    elif order_count == 0:
        segment = "New"

    else:
        segment = "Regular"

    users = {
        'id': id,
        'name': name,
        'orders': orders,
        'order_count': order_count,
        'total_spend': total_spend,
        'avg_basket': avg_basket,
        'segment': segment,
    }
    customer_segmented.append(users)

    segment_count[segment] = segment_count.get(segment, 0) + 1

    if total_spend > highest:
        highest = total_spend
        top_spender = (f"id: {id} , name: {name} , top spend: {highest}")

    if segment != "VIP" and order_count >= 3:
        upsell_candidates.append(users)

print(*customer_segmented, sep='\n')
print(f"segment count: {segment_count}")
print(f"top spend: {top_spender}")
print(*upsell_candidates, sep='\n')

with open('json_customers_segmented.json', 'w') as fp:
    json.dump(customer_segmented, fp)