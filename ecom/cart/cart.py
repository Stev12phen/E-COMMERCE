class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the existing cart from the session
        cart = self.session.get('cart')

        # If the cart does not exist, create an empty one
        if not cart:
            cart = self.session['cart'] = {}

        # Make the cart available on all pages
        self.cart = cart
    def add(self, product):
        product_id= str(product_id)
        if product_id not in self.cart:
            pass
        else:
            self.cart[product_id]= {'price': str(product.price), 'quantity': 1}
        self.session.modified= True

    def __len__(self):
        return len(self.cart)  
