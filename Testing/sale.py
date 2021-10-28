price = float(input("Price: "))
discount_percent = int(input("Discount(%): "))
discount_bath = discount_percent / 100 * price
payment = price - discount_bath
print("Discount(baht): %d" %discount_bath)
print("Payment: %d" %payment) 
