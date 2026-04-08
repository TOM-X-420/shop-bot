from collections import defaultdict

class CartManager:
    def __init__(self):
        self.cart = defaultdict(int)  # holds items and their quantities
        self.orders = []  # keeps track of completed orders

    def add_item(self, item, quantity=1):
        self.cart[item] += quantity
        print(f'Added {quantity} of {item}. Current cart: {dict(self.cart)}')

    def remove_item(self, item, quantity=1):
        if self.cart[item] <= quantity:
            del self.cart[item]
            print(f'Removed {item} from cart as quantity became zero.')
        else:
            self.cart[item] -= quantity
            print(f'Removed {quantity} of {item}. Current cart: {dict(self.cart)}')

    def checkout(self):
        if not self.cart:
            print('Cart is empty. Cannot checkout.')
            return
        order = dict(self.cart)  # convert cart to regular dict to finalize order
        self.orders.append(order)
        self.cart.clear()  # clear cart after checkout
        print(f'Checkout successful. Order placed: {order}')

    def view_cart(self):
        print(f'Current cart: {dict(self.cart)}')

    def view_orders(self):
        print(f'Completed Orders: {self.orders}')

# Example Usage
# cart_manager = CartManager()
# cart_manager.add_item('apple', 3)
# cart_manager.add_item('banana', 2)
# cart_manager.view_cart()
# cart_manager.checkout()
# cart_manager.view_orders()