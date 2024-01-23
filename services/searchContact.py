from services.utils import is_valid_phone_number,is_valid_name

# This service provide search functionality
def searchContact(book:list):
    print("----------------------------------------------")
    print("|                                            |")
    print("- Welcome to 📖 Contact book search section -")
    print("|                                            |")
    print("----------------------------------------------")
    print("\n")

    def searchContact_start():

        search = input("Please provide either phone number or name of the user: ")

        search_result=list()

        if is_valid_name(search):
            search_result=list(filter(lambda x:x['name']==search,book))

            if len(search_result) == 0:
                print(f"\nThere are no records with the name '{search}'. Please try again.\n")
            else:

                print("\nResults are:- ")

                for index, element in enumerate(search_result):

                    print(f"{index+1}. 📃Name: {element['name']}\n   📱Phone Number: {element['phone']}\n   📧Email Address: {element["email"]}\n   🏠Address: {element["address"]}\n")
            
        elif is_valid_phone_number(search):
            search_result=list(filter(lambda x:x['phone']==search,book))

            if len(search_result) == 0:
                print('\nThere is no record with this phone number. Please try again\n')
            else:

                print("\nResults are:- ")

                for index, element in enumerate(search_result):

                    print(f"{index+1}. 📃Name: {element['name']}\n   📱Phone Number: {element['phone']}\n   📧Email Address: {element["email"]}\n   🏠Address: {element["address"]}\n")
        else:
            print("\n❌❌❌ This is not a valid name or phone number. Try again!\n")

        choice = input("Would you like to search again\n\ty for Yes\n\tor press any key to Quit\n==> ")

        if choice.lower() == "y":
            print("\n\n")
            return searchContact_start()
        else:
            print("\n🎉🎉 Thank you for using search service\n")

    searchContact_start()
    