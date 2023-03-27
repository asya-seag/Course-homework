# creating dictionary with items
store_dict = {
    "dress": 120,
    "shirt": 75,
    "skirt": 55,
    "coat": 112
}

#entering money available for customer
money_available = 100

#Welcome the customer and display the items and their prices, along with an option to “exit”
print(f"Welcome to our shop, please view the items \n {store_dict}. ")
exit = input("Would you like to exit our online store?" )
if exit == "yes":
    print("Thank you for visiting our online store!")
elif exit == "no":
    customer_selection = input("Please select your item: ")
else:
     print("Wrong answer, answer yes or no")
# Accept the option as an input, an invalid input should raise a ValueError

total_price=0
try:
        if customer_selection not in store_dict:
            raise ValueError
        else:
            for keys, values in store_dict.items():
                if keys == customer_selection:
                    total_price = total_price + store_dict[keys]
                    print(total_price)


except ValueError:
            print("ValueError, there is no such item in the shop")

# If the customer can afford it, print out a message saying “Here’s your {item}!”

