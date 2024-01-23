

# This service provide view functionality
def viewContacts(book:list):
    print("-------------------------------------------")
    print("|                                         |")
    print("- Welcome to 📖 Contact book view section -")
    print("|                                         |")
    print("-------------------------------------------")
    print("\n")
    if len(book) == 0:
        return print("No contacts in the contact book.\n")

    print("Contacts are:-\n")
    for index, element in enumerate(book):
        print(f"{index+1}. 📃Name: {element['name']}\n   📱Phone Number: {element['phone']}\n   📧Email Address: {element["email"]}\n   🏠Address: {element["address"]}\n")

    print("\n🎉🎉 Thank you for using view service.\n")
