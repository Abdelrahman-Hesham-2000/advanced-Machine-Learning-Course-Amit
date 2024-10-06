address='Amit_ml@gmail.com'
if address.count('@') != 1:
    print("Invalid email")
else:
    username, domain = address.split('@')
    if address.count('.') == 0:
        print("Invalid email")
    else:
        print("Valid email")
print(username)
print(domain)
if address.endswith(".com"):
    print("Commercial")
elif address.endswith(".edu"):
    print("Educational")
else:
    print("Other Domain")