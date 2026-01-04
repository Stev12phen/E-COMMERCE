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
