# creating dictionary with items
store_dict = {
    "dress": 120,
    "shirt": 75,
    "skirt": 55,
    "coat": 112
}

#entering money available for customer
money_available = 100

class WrongInputError(Exception):
    pass
#Welcome the customer and display the items and their prices, along with an option to “exit”
def welcomeToShop():
    print(f"Welcome to our shop, please view the items \n {store_dict}. ")
welcomeToShop()



exit = input("Would you like to exit our online store? (yes/no) " )
if exit == "yes":
    print("Thank you for visiting our online store!")
elif exit == "no":
    customer_selection = input("Please select your item: ")
else:
     raise WrongInputError("Wrong answer, answer yes or no")

# Accept the option as an input, an invalid input should raise a ValueError
def yourselection():
    print("You have selected " + customer_selection)
yourselection()
class WrongItemError(Exception):
    pass


if customer_selection not in store_dict:
    raise WrongItemError ("ValueError, there is no such item in the shop")
else:
    for keys, values in store_dict.items():
        if keys == customer_selection:
            final_price = 0 + store_dict[keys]



class ExceededNumberOfAttemptsError(Exception):
    pass

counter = 0
if final_price <= money_available:
    print(f"Here’s your {customer_selection}!")
    print("Thank you for visiting our online shop")
else:
    for counter in range(3):
        do_you_have_more = int(input("Insufficient funds. Would you like to add more money? Enter a number here:"))
        if do_you_have_more + money_available >= final_price:
            print(f"Here’s your {customer_selection}!")
            print("Thank you for visiting our online shop")
            break


    else:
        raise ExceededNumberOfAttemptsError("Error, too many attempts to add sufficient amount of money")












