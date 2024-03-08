products = {
    1: {'name': "apple", 'price': 19.99,"quantity": 0},
    2: {'name': "banana", 'price': 10.99,"quantity": 10},
    3: {'name': "orange", 'price': 21.99,"quantity": 20},
    4: {'name': "pineapple", 'price': 14.99,"quantity": 0},
    5: {'name': "grapes", 'price': 16.99,"quantity": 0}
}

zero_quantity = [product for product in products.values() if product['quantity'] == 0]
print(zero_quantity)

print(sorted(zero_quantity, key=lambda x  : (x["price"], x["name"])))