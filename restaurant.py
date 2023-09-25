# Restaurant Menu
menu = {
    "1": {"dish": "Pizza", "price": 10.99},
    "2": {"dish": "Burger", "price": 5.99},
    "3": {"dish": "Pasta", "price": 8.99},
    "4": {"dish": "Salad", "price": 6.99},
    "5": {"dish": "Soup", "price": 4.99}
}

# Function to display menu
def display_menu():
    print("Menu:")
    for item, details in menu.items():
        print(f"{item}. {details['dish']}: ${details['price']}")

# Function to place order
def place_order():
    order = []
    while True:
        item = input("Enter the item number (or 'q' to quit): ")
        if item.lower() == "q":
            break
        elif item in menu:
            order.append(menu[item])
        else:
            print("Invalid item number. Please try again.")
    return order

# Function to calculate total bill
def calculate_bill(order):
    total = sum(item['price'] for item in order)
    return total

# Main program
print("Welcome to the Restaurant!")
display_menu()
user_order = place_order()
total_bill = calculate_bill(user_order)
print(f"Total bill: ${total_bill:.2f}")
