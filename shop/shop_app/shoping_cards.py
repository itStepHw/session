class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price)
            }
        self._save()

    def _save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self._save()

    def clear(self):
        self.cart = {}
        self._save()

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def get_items(self):
        return [(product_id, item) for product_id, item in self.cart.items()]

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())