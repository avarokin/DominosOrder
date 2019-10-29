from pizzapi import *
import getpass

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
menu = store.get_menu()

order = Order(store,customer,address)

choice = 0

while True:

    choice = input("\nSelect an option \n1. Add to order \n2.Remove from order \n3. Order complete\n->")

    if choice == "1":
        name = input("Enter search term: ")
        menu.search(Name =name)

        item = input("Enter code of desired item: ")
        menu.add_item(item)

    elif choice == "2":
        item = input("Enter code of item to remove: ")
        menu.remove_item(item)

    elif choice == "3":
        break


print("\n\nEnter payement details: ")

card_numer = input("Enter Debit/Credit card number: ")
expiration = input("Enter expiration in format MMYY: ")
print("Enter three digit pin: ")
cvv = getpass.getpass()
post_code = input("Enter postal code: ")

card = PaymentObject(card_numer,expiration,cvv,post_code)

input("Hit enter to place order, ctrl+c to cancel!")

order.pay_with(card)
