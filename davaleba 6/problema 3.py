from collections import defaultdict
import json

# Read data.txt
with open('data.txt', 'r') as data_file:
    lines = data_file.readlines()

# Dictionaries for processing
user_to_max_amount = defaultdict(int)
user_to_total_value = defaultdict(float)
product_to_total_amount = defaultdict(int)
total_value = 0.0
total_amount = 0
purchase_count = 0

for line in lines:
    parts = line.strip().split(',')
    if len(parts) != 4:
        continue
    user_name = parts[0].strip()
    product_name = parts[1].strip()
    try:
        amount = int(parts[2].strip())
        price = float(parts[3].strip())
    except ValueError:
        continue

    # Update counts
    user_to_max_amount[user_name] = max(user_to_max_amount[user_name], amount)
    user_to_total_value[user_name] += amount * price
    product_to_total_amount[product_name] += amount
    total_value += amount * price
    total_amount += amount
    purchase_count += 1

# a.
if user_to_max_amount:
    max_single_amount = max(user_to_max_amount.values())
    max_single_users = [u for u, v in user_to_max_amount.items() if v == max_single_amount]
else:
    max_single_users = []

# b.
if user_to_total_value:
    max_total_value = max(user_to_total_value.values())
    max_total_users = [u for u, v in user_to_total_value.items() if v == max_total_value]
else:
    max_total_users = []

# c.
average_value = total_value / purchase_count if purchase_count > 0 else 0.0

# d.
average_amount = total_amount / purchase_count if purchase_count > 0 else 0.0

# e.
if product_to_total_amount:
    max_product_amount = max(product_to_total_amount.values())
    most_sold_products = [p for p, v in product_to_total_amount.items() if v == max_product_amount]
else:
    most_sold_products = []

#
stats = {
    "max_single_purchase_users": max_single_users,
    "max_total_value_users": max_total_users,
    "average_purchase_value": average_value,
    "average_purchase_amount": average_amount,
    "most_sold_products": most_sold_products
}

# Write to stats.json
with open('stats.json', 'w', encoding='utf-8') as json_file:
    json.dump(stats, json_file, indent=4, ensure_ascii=False)