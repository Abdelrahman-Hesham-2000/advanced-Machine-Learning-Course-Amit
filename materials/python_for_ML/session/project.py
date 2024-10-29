import random
from prettytable import PrettyTable

u="Dimes"
p="1111"
def login (u,p):
 while True:
    x=input("Name: ")
    
    if x==u:
        y=input("Password: ")
        
        if y==p:
            s=random.randrange(10000,1000000)
            print("Verification code ise: ",s)
            
            while True:
                l=int(input("Enter Verification code: "))
                
                if l==s:
                    print("Welcome")
                    break
                else:
                    print("Incorrect Verification code. Try again.")
            break 
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")   
        
login("Dimes","1111")
products=[
    {"name":"water","price":80.0,"Quantity":1200},
    {"name":"soda","price":130.0,"Quantity":1200},
    {"name":"chips","price":75.0,"Quantity":1200},
    {"name":"bread","price":45.0,"Quantity":1200},
    {"name":"eggs","price":65.0,"Quantity":1200}
]    
table=PrettyTable()
table.field_names=["name","price","Quantity"]
for product in products:
    table.add_row([product["name"],product["price"],product["Quantity"]])

print(table)
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
