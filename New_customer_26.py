age = int(input())
New_customer = bool(input())
if age > 65 and New_customer == False:
    print("The person is eligible for a senior citizen and not new customer")
else:
    print("The person is not eligible")