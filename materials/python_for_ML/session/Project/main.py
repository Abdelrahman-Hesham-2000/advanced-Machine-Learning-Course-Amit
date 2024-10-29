from login import LOGIN
from prettytable import PrettyTable
from app_store import app
x=input("Name: ")
y=input("password: ")
A=LOGIN(x,y)
A.login()
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
app(products)