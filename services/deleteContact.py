from services.utils import is_valid_name,is_valid_phone_number

# This service provide delete functionality
def deleteContact(book:list):

    print("---------------------------------------------")
    print("|                                           |")
    print("- Welcome to 📖 Contact book delete section -")
    print("|                                           |")
    print("---------------------------------------------")
    print("\n")

    def delete_start():
        nonlocal book

        detail=input("Please enter the name or phone of that contact you wants to delete: ")

        if is_valid_name(detail):
            result=list(filter(lambda x:x['name']==detail,book))

            if len(result)==0:
                print(f"\nSorry, name '{detail}' does not exist in our contact book.\n")
            else:

                print("\n📖Found details are: ")

                print(f"   📃Name: {result[0]['name']}\n   📱Phone Number: {result[0]['phone']}\n   📧Email Address: {result[0]["email"]}\n   🏠Address: {result[0]["address"]}\n")


                select_contact=""
                
                while True:
                    select_contact=input(f"\nAre you sure you want to delete the above listed contact from contact book?\nPress:\n\ty for Yes\n\tn for No\n==> ")
                    
                    if select_contact.lower() not in ["y","n"]:
                        print("❌❌❌ Please chose correct fields, please try again!\n")
                    else:
                        break
                if select_contact.lower() == "y":
                    book[:]=list(filter(lambda x:x['name']!=detail,book))

                    print(f"Contact with name '{detail}' deleted successfully✅")

        
        elif is_valid_phone_number(detail):
            result=list(filter(lambda x:x['phone']==detail,book))

            if len(result)==0:
                print(f"\nSorry, phone number '{detail}' does not exist in our contact book.")
            else:

                print("\n📖Found details are:\n")
            
                print(f" 📃Name: {result[0]['name']}\n   📱Phone Number: {result[0]['phone']}\n   📧Email Address: {result[0]["email"]}\n   🏠Address: {result[0]["address"]}\n")

                select_contact=""
                
                while True:
                    select_contact=input(f"\nAre you sure you want to delete the above listed contact from contact book?\nPress:\n\ty for Yes\n\tn for No\n==> ")
                    
                    if select_contact.lower() not in ["y","n"]:
                        print("❌❌❌ Please chose correct fields, please try again!\n")
                    else:
                        break
                if select_contact.lower() == "y":
                    book[:]=list(filter(lambda x:x['phone']!=detail,book))
                    print(f"Contact with phone number '{detail}' deleted successfully✅")


            
        else:
            print("\n❌❌ The format of name or phone number is not valid. Please try again with valid details!")
        
        choice=input("\nDo you want to delete any more contact from contact book.\nPress:\n\ty for Yes\n\tor any other key to quit.\n==> ")

        if choice == "y":
            print("\n\n")
            delete_start()
        else:
            print("\n🎉🎉🎊 Thank to visit delete section\n")
        
    delete_start()
