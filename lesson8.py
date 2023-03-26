# DEMO 1
# def add_vat(vat, prices):
#     """
#     Add commission to every price item in the provided iterable.
#
#     :param vat: float, vat percentage
#     :param prices: iterable, net prices as per customers' receipt
#     :return: list of prices with added vat
#     """
#     new_prices = [(price / 100 * vat) + price for price in prices]
#     return new_prices

# GOOD INPUT
# result = add_vat(vat=20, prices=[24, 0.15, 32.45, 0])
# print(result)

#BAD INPUT
# result = add_vat(vat=20, prices=[24, 0.15, '10', 32.45])
# print(result)

# result = add_vat(vat=20, prices=None)
# print(result)

# result = add_vat(vat=20, prices='abc')
# print(result)

# # DEMO 2
# def apply_discount(product, discount):
#     """
#     Add a discount to the price.
#     :param product: dict obj, item spec including price
#     :param discount: float discount expressed in percent
#     :return: float new price
#     """
#     price = round(product['price'] * (1.0 - (discount / 100)), 2)
#     print(price)
#     assert 0 <= price <= product['price']
#     return price
#
# # Valid input
# # trainers = {'name': 'Running Trainers', 'price': 79.99}
# # discount  = 25 #(represents 25%)
# # print(apply_discount(trainers, discount))
#
# # Invalid input
# # trainers = {'name': 'Running Trainers', 'price': 79.99}
# # discount  = 200 #(represents 200%) --> Assertion Error will be raised
# # print(apply_discount(trainers, discount))
#
# # DEMO 3
# class GymMembership:
#     def __init__(self):
#         self.memberships = {'1': 'Anifah',
#                             '2': 'Anuj'}  # a dictionary of memberships, with ID as key and member name as value
#
#     def membership_exists(self, member_id):
#         """
#         Check whether a membership with the given ID exists.
#         """
#         return member_id in self.memberships
#
#     def find_membership(self, member_id):
#         """
#         Find the membership with the given ID, or return None if not found.
#         """
#         return self.memberships.get(member_id)
#
#     def delete(self, member_id):
#         """
#         Delete the membership with the given ID, if it exists.
#         """
#         if member_id in self.memberships:
#             del self.memberships[member_id]
#
# class User:
#     def __init__(self, name, isAdmin):
#         self.name = name
#         self.isAdmin = isAdmin
#
#     def is_admin(self):
#         """
#         Check whether the user is an admin.
#         """
#         return self.isAdmin
#
#
# gym_members = GymMembership()
#
#
# # def cancel_membership(membership_id, user):
# #     """
# #     Canel Gym membership for an existing member.
# #     """
# #
# #     assert user.is_admin(), 'Must be admin to cancel'
# #     assert gym_members.membership_exists(membership_id), 'Unknown id'
# #     gym_members.delete(membership_id)
# #     print("User deleted, new user list: {}".format(gym_members.memberships))
# #
# # user = User('random', False)
# # cancel_membership('5', user)
#
# # DEMO 4
# class AuthorisationError(Exception): # don't worry about this syntax yet
#     pass
#
# gym_members = GymMembership()
#
# def cancel_membership(membership_id, user):
#     """
#     Canel Gym membership for an existing member.
#     """
#     if not user.is_admin():
#         raise AuthorisationError('Must be admin to cancel')
#     if not gym_members.membership_exists(membership_id):
#         raise ValueError('Unknown id')
#
#     gym_members.delete(membership_id)
#     print("User deleted, new user list: {}".format(gym_members.memberships))
#
# # user = User('random', False)
# # cancel_membership('5', user)
#
# # user = User('random', True)
# # cancel_membership('5', user)
#
# # user = User('random', True)
# # cancel_membership('1', user)

# DEMO 6 - try / except

# denominator = int(input("Please eneter a number to divide by: "))
# try:
#     division_result = 100 / denominator
#     print(division_result)
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")

# try with multiple excepts
# user_input = input("Please eneter a number to divide by: ")
# print(user_input)
# try:
#     denominator = int(user_input)
#     division_result = 100 / denominator
#     print(division_result)
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")
# except ValueError:
#     print("You cannot divide by a non-numeric value, please try again")


# DEMO 7 -- raise exception
# number = int(input('Enter a number in the range 5-10: '))
#
# try:
#     if number < 5 or number > 10:
#         raise Exception
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
#
# except:
#     print("Your number is NOT in the requested range")


# class ValueIsBelowHundredError(ValueError):
#     """Raise when value is below 100"""
#     pass
#
#
# # Testing our exception
# number = int(input('Enter a number above 100: '))
#
# try:
#     if number < 100:
#         raise ValueIsBelowHundredError
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")

#Demo - debugging
# def debugging_n_breakpoints():
#     my_list = []
#     for i in range(10):
#         new_i = 10 + i
#
#         import pdb
#         pdb.set_trace()
#
#         print('new value is: ', i)
#         my_list.append((new_i))
#     return my_list
#
# print(debugging_n_breakpoints())



#Excercises
# Exercise 1
def validate_name(name):
    if ',' not in name:
        raise ValueError("Incorrect input: missing ',' to separate first name and last name")

    names = name.split(',')
    if len(names[0]) < 1 or len(names[1]) < 1:
        raise ValueError("Incorrect input: missing first name or surname value")

def validate_age(age):
    if age < 0:
        raise ValueError("Incorrect input: only positive values allowed")
    assert age > 12 and age < 20
try:
    is_reg_successful = False
    name = input("Please enter your first name and last name separated by comma:")
    validate_name(name)
    age = int(input('Please enter your age:'))
    validate_age(age)
except ValueError as error:
    print("Invalid input {}".format(error))
except AssertionError as error:
    print("The age is not within the 'teenager' category")
else:
    with open('registration.txt', "a+") as file:
        file.write("New member name: {} and age {} \n".format(name, age))
        is_reg_successful = True
finally:
    if is_reg_successful:
        print("Registration Process completed SUCCESSFULLY")
    else:
        print("Could not complete registration.Please try again")