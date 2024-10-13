address='Amit_ml@gmail.edu'
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
#here you can use another way ..... 
''' 
domain_types = [
        (".com", "Commercial"),
        (".edu", "Educational"),
        (".org", "Organization"),
        (".gov", "Government")
    ]

    # Loop through the list of domain types and check if address ends with any of them
    for domain, domain_name in domain_types:
        if address.endswith(domain):
            print(f"This is a {domain_name} domain")
            return  # Exit once the domain type is found

    # If none of the above match, print "Other Domain"
    print("Other Domain")
'''

if address.endswith(".com"):
    print("Commercial")
elif address.endswith(".edu"):
    print("Educational")
else:
    print("Other Domain")
