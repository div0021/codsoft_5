from services.utils import is_valid_phone_number,is_valid_email,is_valid_name

# This service provide update functionality
def updateContact(book:list):
    print("---------------------------------------------")
    print("|                                           |")
    print("- Welcome to 📖 Contact book update section -")
    print("|                                           |")
    print("---------------------------------------------")
    print("\n")

    def update_start():
        nonlocal book

        detail=input("Please enter the name or phone of that contact you wants to update: ")

        if is_valid_name(detail):
            result=list(filter(lambda x:x['name']==detail,book))

            if len(result)==0:
                print("\nSorry, this name does not exist in our contact book.")
            else:

                print("\n📖Found details are: ")

                print(f"   📃Name: {result[0]['name']}\n   📱Phone Number: {result[0]['phone']}\n   📧Email Address: {result[0]["email"]}\n   🏠Address: {result[0]["address"]}\n")


                def updateInfo():
                    nonlocal result
                    nonlocal book
                
                    select =""

                    while True:

                        select = input("\nPlease enter the field you want to update.\nPress:\n\t1 to 📃name\n\t2 to the 📱phone number\n\t3 to 📧email\n\t4 to 🏠address\n ==> ")

                        if select not in ["1","2","3","4"]:
                            print("\n❌❌ Please enter a valid field. ❌❌")
                        else:
                            break
                    
                    book=list(filter(lambda x:x['name']!=detail,book))
                    
                    if select == "1":
                        newName=""
                        while True:
                            newName=input("\nEnter the new name for this person: ")

                            if not is_valid_name(newName):
                                print("❌❌ This is not a valid name. Name only contain alphabets and in between space only. Please try again with a valid name.")
                            else:
                                break
                        result[0]['name']=newName
                        book.append(result[0])
                        print(f"📃Name update successfully.")
                    elif select == "2":
                        newPhone=""
                        while True:
                            newPhone=input("\nEnter the new phone number for this person: ")

                            if not is_valid_phone_number(newPhone):
                                print("❌❌ This is not a valid phone number. Number should contain atleast 10 digits. Please try again with a valid phone number.")
                            else:
                                break
                        result[0]['phone']=newPhone
                        book.append(result[0])
                        print(f"📱Phone number update successfully.")
                    elif select == "3":
                        newEmail=""
                        while True:
                            newEmail=input("\nEnter the new email for this person: ")

                            if not is_valid_email(newEmail):
                                print("❌❌ This is not a valid email. Please try again with a valid name.")
                            else:
                                break
                        result[0]['email']=newEmail
                        book.append(result[0])
                        print(f"📧Email update successfully.")
                    elif select == "4":
                        newAddress=""
                        while True:
                            newAddress=input("\nEnter the new address for this person: ")

                            if len(newAddress)==0:
                                print("❌❌ Please enter a valid address.")
                            else:
                                break
                        result[0]['address']=newAddress
                        book.append(result[0])
                        print(f"🏠Address updated successfully✅")
                    
                    print("\nUpdated details are:\n")
                    print(f"   📃Name: {result[0]['name']}\n   📱Phone Number: {result[0]['phone']}\n   📧Email Address: {result[0]["email"]}\n   🏠Address: {result[0]["address"]}\n")

                
                updateInfo()
        
        elif is_valid_phone_number(detail):
            result=list(filter(lambda x:x['phone']==detail,book))

            if len(result)==0:
                print("\nSorry, this phone number does not exist in our contact book. Try again\n")
            else:

                print("\n📖Found details are:\n")
            
                print(f" 📃Name: {result[0]['name']}\n   📱Phone Number: {result[0]['phone']}\n   📧Email Address: {result[0]["email"]}\n   🏠Address: {result[0]["address"]}\n")


                def updateInfo():
                    nonlocal result
                    nonlocal book
                
                    select =""

                    while True:

                        select = input("\nPlease enter the field you want to update.\nPress:\n\t1 for 📃name\n\t2 for the 📱phone number\n\t3 for 📧email\n\t4 for 🏠address\n ==> ")

                        if select not in ["1","2","3","4"]:
                            print("\n❌❌ Please enter a valid field. ❌❌")
                        else:
                            break
                    
                    book=list(filter(lambda x:x['name']!=detail,book))
                    
                    if select == "1":
                        newName=""
                        while True:
                            newName=input("\nEnter the new name for this person: ")

                            if not is_valid_name(newName):
                                print("❌❌ This is not a valid name. Name only contain alphabets and in between space only. Please try again with a valid name.")
                            else:
                                verify_name=list(filter(lambda x:x['name']==newName,book))
                                if len(verify_name) != 0:
                                    print(f"❌❌ This name '{newName}' already exist, try another one!\n")
                                else:
                                    break


                        result[0]['name']=newName
                        book.append(result[0])
                        print(f"📃Name updated successfully.")


                    elif select == "2":
                        newPhone=""
                        while True:
                            newPhone=input("\nEnter the new phone number for this person: ")

                            if not is_valid_phone_number(newPhone):
                                print("❌❌ This is not a valid phone number. Number should contain atleast 10 digits. Please try again with a valid phone number.")
                            else:
                                verify_phone=list(filter(lambda x:x['phone']==newPhone,book))
                                if len(verify_phone) != 0:
                                    print(f"❌❌ This name '{newPhone}' already exist, try another one!\n")
                                else:
                                    break
                        result[0]['phone']=newPhone
                        book.append(result[0])
                        print(f"📱Phone number updated successfully.")
                    elif select == "3":
                        newEmail=""
                        while True:
                            newEmail=input("\nEnter the new email for this person: ")

                            if not is_valid_email(newEmail):
                                print("❌❌ This is not a valid email. Please try again with a valid name.")
                            else:
                                break
                        result[0]['email']=newEmail
                        book.append(result[0])
                        print(f"📧Email update successfully.")
                    elif select == "4":
                        newAddress=""
                        while True:
                            newAddress=input("\nEnter the new address for this person: ")

                            if len(newAddress)==0:
                                print("❌❌ Please enter a valid address.")
                            else:
                                break
                        result[0]['address']=newAddress
                        book.append(result[0])
                        print(f"🏠Address updated successfully✅")
                    
                    print("\nUpdated details are:\n")
                    print(f"   Name: {result[0]['name']}\n   Phone Number: {result[0]['phone']}\n   Email Address: {result[0]["email"]}\n   Address: {result[0]["address"]}\n")

                
                updateInfo()
        else:
            print("\n❌❌ The format of name or phone number is not valid. Please try again with valid details!")
        
        choice=input("\nDo you want to update any more contact details.\nPress:\n\ty for Yes\n\tor press any other key to quit.\n==> ")

        if choice == "y":
            print("\n\n")
            update_start()
        else:
            print("\n🎉🎉🎊 Thank for using update service\n")
    
    update_start()
