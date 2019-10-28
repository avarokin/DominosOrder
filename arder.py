from pizzapi import *

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")
number = input("Enter phone number: ")

customer = Customer(first_name,last_name,email,number)

street = input("Enter street address: ")
city = input("Enter city: ")
state = input("Enter state: ")
post_code = input("Enter postal code: ")

address = Address(street,city,state,post_code)

store = address.closest_store()

