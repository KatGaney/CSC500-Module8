class ItemToPurchase:
    """Represents an item with a name, price, quantity, and optional description."""

    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        price_str = f"{self.item_price:.0f}" if self.item_price.is_integer() else f"{self.item_price:.2f}"
        total_str = f"{total_cost:.0f}" if total_cost.is_integer() else f"{total_cost:.2f}"
        print(f"{self.item_name} {self.item_quantity} @ ${price_str} = ${total_str}")


class ShoppingCart:
    """Represents a customer's shopping cart with items, name, and date."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Cart operations
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Totals and descriptions
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")
            return

        total_cost = 0
        for item in self.cart_items:
            subtotal = item.item_price * item.item_quantity
            price_str = f"{item.item_price:.0f}" if item.item_price.is_integer() else f"{item.item_price:.2f}"
            subtotal_str = f"{subtotal:.0f}" if subtotal.is_integer() else f"{subtotal:.2f}"
            print(f"{item.item_name} {item.item_quantity} @ ${price_str} = ${subtotal_str}")
            total_cost += subtotal

        print(f"Total: ${total_cost:.0f}" if total_cost.is_integer() else f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Input validation
def get_string(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass


# Initial two-item setup
def get_two_items():
    print("Item 1")
    name1 = get_string("Enter the item name:\n")
    price1 = get_float("Enter the item price:\n")
    qty1 = get_int("Enter the item quantity:\n")
    item1 = ItemToPurchase(name1, price1, qty1)

    print("\nItem 2")
    name2 = get_string("Enter the item name:\n")
    price2 = get_float("Enter the item price:\n")
    qty2 = get_int("Enter the item quantity:\n")
    item2 = ItemToPurchase(name2, price2, qty2)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"Total: ${total:.0f}" if total.is_integer() else f"Total: ${total:.2f}")

    return item1, item2


# Menu interaction
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            print("ADD ITEM TO CART")
            name = get_string("Enter the item name:\n")
            desc = input("Enter the item description:\n").strip() or "none"
            price = get_float("Enter the item price:\n")
            qty = get_int("Enter the item quantity:\n")
            cart.add_item(ItemToPurchase(name, price, qty, desc))

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = get_string("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = get_string("Enter the item name:\n")
            new_qty = get_int("Enter the new quantity:\n")
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=new_qty))

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            break


# Main program
if __name__ == "__main__":
    print("Enter customer's name:")
    customer_name = get_string("")
    print("Enter today's date:")
    current_date = get_string("")

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    shopping_cart = ShoppingCart(customer_name, current_date)

    item1, item2 = get_two_items()
    shopping_cart.add_item(item1)
    shopping_cart.add_item(item2)

    print_menu(shopping_cart)
