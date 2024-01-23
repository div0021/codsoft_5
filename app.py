from services.addContact import addContact
from services.deleteContact import deleteContact
from services.searchContact import searchContact
from services.updateContact import updateContact
from services.viewContacts import viewContacts


def contact_book(book: list):
    print("\n\n--------------------------------------")
    print("|                                    |")
    print("- Welcome to 📖 Contact book section -")
    print("|                                    |")
    print("--------------------------------------")
    print("\n")

    print("👋👋Hi, This is our contact book app")
    print(
        "The contact book app is a user-friendly tool that allows individuals to efficiently organize and manage contacts, offering features such as quick search, seamless communication integration. Users can effortlessly store, retrieve, update and delete contact information, ensuring they stay connected and organized on the go.\n"
    )

    def operations():
        nonlocal book

        chose = input(
            "\nPlease Chose the operation to perform.\nPress:\n\t1 to ➕ add contact in contact book\n\t2 to 👁️  view all the contacts present in contact book\n\t3 to 🔎 search a specific contact in contact book\n\t4 to 📝 update a contact in contact book\n\t5 to 🗑️  delete a specific contact in contact book\n==> "
        )

        if chose not in ["1", "2", "3", "4", "5"]:
            print(
                "❌❌❌ Invalid operation, please chose suitable operation, try again!\n"
            )
            operations()

        if chose == "1":
            print("\n\n")
            print("###################################\n")
            addContact(book)
            print("###################################\n\n")
        elif chose == "2":
            print("\n\n")
            print("###################################\n")
            viewContacts(book)
            print("###################################\n\n")
        elif chose == "3":
            print("\n\n")
            print("###################################\n")
            searchContact(book)
            print("###################################\n\n")
        elif chose == "4":
            print("\n\n")
            print("###################################\n")
            updateContact(book)
            print("###################################\n\n")
        else:
            print("\n\n")
            print("###################################\n")
            deleteContact(book)
            print("###################################\n\n")

        select = input(
            "Do you want to perform any other operation on the contact book?\nPress:\n\t✅ y for Yes\n\t❌ any other key to Quit\n==> "
        ).lower()

        if select == "y":
            operations()

    operations()


if __name__ == "__main__":
    book = [{
        'name': 'tom',
        'phone': '9949499949',
        'email': '123@qq.com',
        'address': '124, bhubaneshwar'
    }]

    contact_book(book)
    print("\n🎊🎉🎉 Thank you for visiting, 👋👋 Byee...")
