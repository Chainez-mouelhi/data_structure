import unittest
def produits_rupture_de_stock(inventaire):
    return sorted([(id_produit, info_produit) for id_produit, info_produit in inventaire.items() if info_produit['quantity'] == 0], key=lambda x: (x[1]['price'], -x[0]))


class TestProduitsRuptureDeStock(unittest.TestCase):

    def test_produits_rupture_de_stock(self):
        products = {
            1: {'name': "apple", 'price': 19.99, "quantity": 0},
            2: {'name': "banana", 'price': 10.99, "quantity": 10},
            3: {'name': "orange", 'price': 21.99, "quantity": 20},
            4: {'name': "pineapple", 'price': 14.99, "quantity": 0},
            5: {'name': "grapes", 'price': 16.99, "quantity": 0}
        }
        expected_result = [(1, {'name': "apple", 'price': 19.99, "quantity": 0})]
        self.assertEqual(produits_rupture_de_stock(products), expected_result)

    def test_produits_non_rupture_de_stock(self):
        products = {
            1: {'name': "apple", 'price': 19.99, "quantity": 5},
            2: {'name': "banana", 'price': 10.99, "quantity": 10},
            3: {'name': "orange", 'price': 21.99, "quantity": 20},
            4: {'name': "pineapple", 'price': 14.99, "quantity": 8},
            5: {'name': "grapes", 'price': 16.99, "quantity": 15}
        }
        self.assertEqual(produits_rupture_de_stock(products), [])

if __name__ == '__main__':
    unittest.main()
