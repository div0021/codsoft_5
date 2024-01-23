from services.utils import is_valid_email, is_valid_name, is_valid_phone_number


# This service provide add functionality
def addContact(book: list):

    print("------------------------------------------")
    print("|                                        |")
    print("- Welcome to 📖 Contact book add section -")
    print("|                                        |")
    print("------------------------------------------")
    print("\n")

    def add_service():

        print("Okay, provide necessary details of the user ->\n")

        name = ""
        phone = ""
        address = ""
        email = ""
        while True:
            name = input("📃Username: ").strip()
            if not is_valid_name(name):
                print("❌❌❌ Not valid name ❌❌❌, please try again!\n")
            else:
                verify_name = list(filter(lambda x: x['name'] == name, book))
                if len(verify_name) != 0:
                    print(
                        "❌❌ This name already exist in contact book, please try again with different name!\n"
                    )
                else:
                    break
        while True:
            phone = input("📱Phone number: ")

            if not is_valid_phone_number(phone):
                print("❌❌❌ Not valid phone number ❌❌❌, please try again!\n")
            else:
                verify_phone = list(filter(lambda x: x['phone'] == phone,
                                           book))
                if len(verify_phone) != 0:
                    print(
                        "❌❌ This phone number already exists in contact book, please try again with different phone number!\n"
                    )
                else:
                    break

        while True:
            email = input("📧Email: ")
            if not is_valid_email(email):
                print("❌❌❌ Not valid email ❌❌❌, please try again!\n")
            else:
                break
        while True:
            address = input("🏠Address: ")
            if len(address) == 0:
                print("❌❌❌ Not valid address ❌❌❌, please try again!\n")
            else:
                break

        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        book.append(contact)
        print("\nContact added successfully✅")

        choice = input(
            "\nDo you want to add more contact in contact book?\nPress:\n\ty for Yes\n\tany other key to Quit\n==> "
        )

        if choice == "y":
            print("\n")
            add_service()
        else:
            print("\n🎉🎉 Thank you for using add service.\n")

    add_service()
