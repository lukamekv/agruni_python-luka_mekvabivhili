from functools import reduce

products = [
    ("Keyboard",    49.99,  3),
    ("Mouse",       19.99,  0),
    ("Monitor",    159.99,  2),
    ("USB Cable",    4.99, 10),
    ("Headphones",  89.99,  1)
]

# 1) მარაგში არსებული პროდუქტები
in_stock = list(filter(lambda p: p[2] > 0, products))

# 2) თითოეული პროდუქტის ჯამური ღირებულება
total_values = list(map(lambda p: (p[0], round(p[1] * p[2], 2)), in_stock))

# 3) მთლიანი ღირებულება
total = reduce(lambda acc, p: acc + p[1] * p[2], in_stock, 0)

# ბეჭდვა
print("1) მარაგშია:", [p[0] for p in in_stock])
print("2) ჯამური ღირებულება:")
for name, value in total_values:
    print(f"   {name:12} → {value:6.2f} GEL")
print(f"3) სულ მაღაზიაში: {total:.2f} GEL")