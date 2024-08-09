from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(Shop.__file_name, 'r') as file:
                products = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            products = []
        return products

    def add(self, *products):
        current_products = self.get_products()
        current_product_names = [product.split(', ')[0] for product in current_products]

        with open(Shop.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product.name not in current_product_names:
                    file.write(product_str + '\n')
                    current_product_names.append(product.name)
                else:
                    print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

products = s1.get_products() #переделала по-своему
for product in products:
    print(product)
