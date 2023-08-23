class MenuItem:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class CoffeeShop:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, name, price, description):
        menu_item = MenuItem(name, price, description)
        self.menu.append(menu_item)

    def display_menu(self):
        print(f"Welcome to {self.name}! Here is our menu:")
        for item in self.menu:
            print(f"{item.name} - IDR {item.price} - {item.description}")

    def take_order(self, customer_name, order_items):
        order_items = order_items.split(',')
        order_items = [item.strip() for item in order_items]
        order_summary = {}
        order_total = 0

        for order in order_items:
            item_name, quantity = order.split(':')
            quantity = int(quantity)
            menu_item = next((item for item in self.menu if item.name == item_name), None)
            
            if menu_item:
                order_item = OrderItem(menu_item, quantity)
                order_summary[item_name] = order_item
                order_total += menu_item.price * quantity
            else:
                print(f"Sorry, {item_name} is not in the menu.")
                return

        self.orders.append({'customer_name': customer_name, 'order_summary': order_summary, 'order_total': order_total})
        print(f"Thank you for your order, {customer_name}! Your total is IDR {order_total}.")

    def display_orders(self):
        print("Here are the current orders:")
        for order in self.orders:
            print(f"{order['customer_name']} ordered:")
            for item_name, order_item in order['order_summary'].items():
                print(f"{order_item.quantity} {item_name}(s) - Total: IDR {order_item.menu_item.price * order_item.quantity}")
            print(f"Total: IDR {order['order_total']}")

# Create coffee shop instance
my_coffee_shop = CoffeeShop("Brewtopia")

# Add menu items with descriptions
my_coffee_shop.add_menu_item("Latte", 20000, "Smooth espresso with steamed milk")
my_coffee_shop.add_menu_item("Cappuccino", 18000, "Espresso topped with foamed milk")
my_coffee_shop.add_menu_item("Espresso", 15000, "Strong and concentrated coffee")
my_coffee_shop.add_menu_item("Mocha", 22000, "Espresso with chocolate and milk")
my_coffee_shop.add_menu_item("Iced Coffee", 17000, "Chilled brewed coffee with ice")
my_coffee_shop.add_menu_item("Croissant", 12000, "Buttery and flaky pastry")
my_coffee_shop.add_menu_item("Sandwich", 15000, "Fresh and delicious sandwich")
my_coffee_shop.add_menu_item("Brownie", 10000, "Rich chocolate brownie")

# Display menu
my_coffee_shop.display_menu()

# Take orders
while True:
    customer_name = input("Enter your name: ")
    if customer_name.lower() == "exit":
        break
    order_items = input("Enter your order items and quantities (item:quantity, separated by commas): ")
    my_coffee_shop.take_order(customer_name, order_items)

# Display orders
my_coffee_shop.display_orders()
