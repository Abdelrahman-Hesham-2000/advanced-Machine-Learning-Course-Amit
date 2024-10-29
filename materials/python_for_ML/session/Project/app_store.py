def app(products):
 total_discounted_price = 0
 while True:
    product_name = input("Enter Product Name: ").lower()

    # Check if the entered product exists in the list
    if product_name not in map(lambda x: x["name"].lower(), products):
        print("Product not found in the table. Please enter a valid product.")
        continue

    quantity_required = float(input("Enter Quantity Required: "))

    # Locate each input with saved data
    product = next(p for p in products if p["name"].lower() == product_name)

    # Check if the entered quantity is greater than the available quantity
    if quantity_required > product["Quantity"]:
        print("Insufficient quantity. Please enter a new quantity.")
        continue

    # 5% discount for every 250 quantity (CALCULATIONS)
    discount_quantity = quantity_required // 250
    discount_percentage = 5.0 * discount_quantity
    total_discount = min(discount_percentage, 25.0)  # Cap the discount at 25%
    discounted_price = quantity_required * product["price"] * (1 - total_discount / 100)
    # Updated list after purchase
    product["Quantity"] -= quantity_required

    # total of the Added discounted price
    total_discounted_price += discounted_price

    print(f"Discounted Price: ${discounted_price:.2f}")