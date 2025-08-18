class shop:
    shoping_mal = "jamuna"  # class attribute (shared by all objects)

    def __init__(self, buyer):
        self.buyer = buyer   # instance attribute (different for each buyer)
        self.cart = []       # instance attribute (each buyer has their own cart)

    def add_to_cart(self, item):
        self.cart.append(item)  # add new item to the cart list


# Create an object for buyer "Shanto"
s1 = shop("Shanto")
s1.add_to_cart("cap")       # Shanto adds "cap" to his cart
s1.add_to_cart("i phone")   # Shanto adds "i phone" to his cart
s1.add_to_cart("macbook")   # Shanto adds "macbook" to his cart
print(s1.cart)              # Output: ['cap', 'i phone', 'macbook']


# Create another object for buyer "Riyad"
s2 = shop("Riyad")
s2.add_to_cart("watch")     # Riyad adds "watch" to his cart
s2.add_to_cart("shoes")     # Riyad adds "shoes" to his cart
s2.add_to_cart("T shirt")   # Riyad adds "T shirt" to his cart
print(s2.cart)              # Output: ['watch', 'shoes', 'T shirt']
