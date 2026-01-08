# PYTHON Restaurant Management System

menu = {
    "espresso": 120,
    "cappuccino": 150,
    "latte": 160,
    "cold coffee": 180,
    "veg sandwich": 140,
    "cheese sandwich": 160,
    "french fries": 130,
    "pasta": 220,
    "veg burger": 190,
    "chocolate muffin": 110
}

order = {}

print("\n" + "=" * 45)
print("        ☕ WELCOME TO PYTHON RESTAURANT ☕")
print("=" * 45)

print("\n📋 MENU")
print("-" * 45)
for item, price in menu.items():
    print(f"{item.title():20} : ₹{price}")
print("-" * 45)

while True:
    item = input("\nEnter item name (or 'exit' to finish): ").lower()

    if item == "exit":
        break

    if item in menu:
        qty = int(input(f"Enter quantity for {item.title()}: "))
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        print(f"✅ {item.title()} x{qty} added to your order")
    else:
        print("❌ Item not available. Please choose from the menu.")

print("\n" + "=" * 45)
print("              🧾 BILL SUMMARY")
print("=" * 45)

subtotal = 0
for item, qty in order.items():
    price = menu[item] * qty
    subtotal += price
    print(f"{item.title():20} x{qty} = ₹{price}")

gst = subtotal * 0.05
total = subtotal + gst

print("-" * 45)
print(f"{'Subtotal':25} : ₹{subtotal}")
print(f"{'GST (5%)':25} : ₹{gst:.2f}")
print(f"{'Total Amount':25} : ₹{total:.2f}")
print("-" * 45)

print("\n🙏 Thank you for dining with PYTHON Restaurant!")
print("⭐ Visit Again ⭐")
