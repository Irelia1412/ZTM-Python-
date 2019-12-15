from FUN import Profile
from PIL import Image
import random
import smtplib
from email.message import EmailMessage
import re



def main():
    id= 1
    lis=[]
    swtich = True
    print("Welcome to my program !")
    print("--------------------------------------------")
    while(swtich):
        #with open('database.txt', 'r') as data:

            print("Enter one of the following options: ")
            print("1. Add profile")
            print("2. Display recent profiles")
            print("3. Search for a profile")
            print("4. Update profile")
            print("5. Remove profile")
            print("6. Remove All")
            print("7. Pictures")
            print("8. Resize pictures")
            print("9. Random number game")
            print("10. Sending Email for all profiles")
            print("11. Exit")
            option=  int(input("Your options: "))


            if (option == 1): # add into the list

                    def enterlis():
                        with open('database.txt', 'a') as database:

                            fname = str(input("Enter your first name: "))
                            lname = str(input("Enter your last name: "))
                            age = int(input("Enter your age: "))
                            email = str(input("Enter your email without writing @gmail.com: "))+"@gmail.com"
                            hobby = str(input("Enter your hobby: "))

                            #database.write('ID: ' + str(id) + "\n")
                            #database.write("First Name: "+fname+ "\n")
                            #database.write("Last Name: "+lname+"\n")
                            #database.write("Age: "+str(age)+"\n")
                            #database.write("Email: "+email+"\n")
                            #database.write("Hobby: "+hobby+"\n")
                            #database.write("--------------------------------------------\n")

                            return lis.append(Profile(id, fname, lname, age, email, hobby))

                            print("")
                    enterlis()
                    print("")
                    id=id+1

                    #info = data.read()

                    #x = re.findall("ID: [0-9]+", info)

                    #if not x:
                        #enterlis()

                    #else:
                        #x = x[-1]
                        #x.split("ID: ")
                        #x = int(x[4:]) + 1
                        #id = x
                        #enterlis()





            elif (option == 2):  # search for an object in the list

                 print("\n")
                 for obj in lis:
                    print("--------------------------------------------")
                    print(f"ID: {obj.id}")
                    print(f"First Name: {obj.fname}")
                    print(f"Last Name: {obj.lname}")
                    print(f"Age: {obj.age}")
                    print(f"Email: {obj.email}")
                    print(f"Hobby: {obj.hobby}")
                    print("--------------------------------------------")

                    print("\n")

            elif(option == 3): # search for an object in the list
                print("\n")
                enter=int(input("Enter the ID you want to display: "))
                for obj in lis:

                    if(enter==obj.id):
                        print("--------------------------------------------")
                        print(f"ID: {obj.id}")
                        print(f"First Name: {obj.fname}")
                        print(f"Last Name: {obj.lname}")
                        print(f"Age: {obj.age}")
                        print(f"Email: {obj.email}")
                        print(f"Hobby: {obj.hobby}")
                        print("--------------------------------------------")

                        print("\n")

            elif (option == 4):
                print("")
                update = int(input("Enter the ID you want to update profile: "))
                for obj in lis:
                    if update == obj.id:
                        print("Enter the following options: ")
                        print("1. Update First Name")
                        print("2. Update Last Name")
                        print("3. Update Age")
                        print("4. Update Email")
                        print("5. Update Hobby")
                        print("6. Exit")
                        print("\n")
                        option5 = int(input("Enter the following options: "))
                        print("\n")
                        if option5 == 1:
                            obj.fname = str(input("Enter the First Name : "))
                        if option5 == 2:
                            obj.lname = str(input("Enter the Last Name : "))
                        if option5 == 3:
                            obj.age = int(input("Enter the Age : "))
                        if option5 == 4:
                            obj.email = str(input("Enter the Email without @gmail.com : ")+'@gmail.com')
                        if option5 == 5:
                            obj.hobby = str(input("Enter the Hobby : "))
                        if option5 == 6:
                            continue
                            print("EXIT")
                            print("\n")


            elif(option==5): # remove an object from the list
                enter= int(input("Enter the ID you want to delete the list: "))
                for obj in lis:
                    if (enter==obj.id):
                        lis.remove(obj)
                        print("\n")

            elif(option==6): # clear the list
                lis.clear()
                print("\n")

            elif (option == 7): # image opening
                print("Enter one of the following Images you want to display: ")
                print("1. Irelia")
                print("2. Irelia Mirror")
                print("3. IG Irelia")
                print("4. Exit")
                print("")
                option2 = int(input("Your option: "))
                if(option2 == 1):
                    ima = Image.open('Screen Shot 1441-03-13 at 3.10.09 PM copy.png')
                    ima.show()
                    print("\n")

                elif(option2 == 2):
                    ima2 = Image.open('157338784156073568 copy.png')
                    ima2.show()
                    print("\n")

                elif(option2 == 3):
                    ima3 = Image.open('Screen Shot 1441-01-28 at 3.03.54 PM copy.png')
                    ima3.show()
                    print("\n")

                elif(option2 == 4):
                    continue
                    print("\n")

                else:
                    print("You have entered wrong number please try again")
                    print("\n")


            elif (option == 8): # image resizing with thumbnailing
                print("Enter one of the following Images you want to display: ")
                print("1. Resize Irelia")
                print("2. Resize  Irelia Mirror")
                print("3. Resize  IG Irelia")
                print("4. Exit")
                print("\n")
                option3 = int(input("Your option: "))
                print("\n")

                if (option3 == 1):
                    imag = Image.open('Screen Shot 1441-03-13 at 3.10.09 PM copy.png')
                    he = int(input("Enter height: "))
                    wi = int(input("Enter Width: "))
                    imag.thumbnail((he, wi))
                    imag.save(str(input("Enter the file name you want to save: " )) + ".png")
                    imag.show()
                    print("\n")

                elif (option3 == 2):
                    imag2 = Image.open('157338784156073568 copy.png')
                    he2 = int(input("Enter height: "))
                    wi2 = int(input("Enter Width: "))
                    imag2.thumbnail((he2, wi2))
                    imag2.save(str(input("Enter the file name you want to save: " )) + ".png")
                    imag2.show()
                    print("\n")
                elif (option3 == 3):
                    imag3 = Image.open('Screen Shot 1441-01-28 at 3.03.54 PM copy.png')
                    he3 = int(input("Enter height: "))
                    wi3 = int(input("Enter Width: "))
                    imag3.thumbnail((he3, wi3))
                    imag3.save(str(input("Enter the file name you want to save: " )) + ".png")
                    imag3.show()
                    print("\n")
                elif (option3 == 4):
                    continue
                    print("\n")
                else:
                    print("You have entered wrong number please try again")
                    print("\n")

            elif (option == 9): # random game
                counter= 1
                switch2=True
                print("Welcome to the random number game !")
                print("Guess the number to win the game !")
                print("If you want to leave the game press 0\n")
                print("Enter the following options: ")

                print("1. 1-10")
                print("2. 1-50")
                print("3. 1-100")
                option4 = int(input("Your option: "))

                print("\n")

                if(option4 == 1):


                    while(switch2): # 1 - 10 game
                        random_number = int(random.randint(1, 10))

                        enter=int(input(("Enter numbers from 1-10: ")))
                        print("\n")
                        if(enter == random_number):
                            print(f"WOOO You won it with record {counter} times\n")
                            switch2= False
                            print("\n")
                        elif(enter == 0):
                            switch2 = False
                            print("Thank you for playing this game !")
                            print("\n")
                        else:
                            print("Wrong >.< Try again !\n")
                            print("\n")

                        counter = counter +1
                        print("")


                elif (option4 == 2): # 1 - 50 game

                    while (switch2):
                        random_number = int(random.randint(1, 50))

                        enter2 = int(input(("Enter numbers from 1-50: ")))
                        print("")
                        if (enter2 == random_number):
                            print(f"WOOO You won it with record {counter} times\n")
                            switch2 = False
                            print("")
                        elif (enter2 == 0):
                            switch2 = False
                            print("Thank you for playing this game !")
                            print("")
                        else:
                            print("Wrong >.< Try again !\n")
                            print("")

                        counter = counter + 1

                        print("")

                elif (option4 == 3): # 1 - 100 game

                    while (switch2):
                        random_number = int(random.randint(1, 100))

                        enter3 = int(input(("Enter numbers from 1-50: ")))
                        print("")
                        if (enter3 == random_number):
                            print(f"WOOO You won it with record {counter} times\n")
                            switch2 = False
                            print("")
                        elif (enter3 == 0):
                            switch2 = False
                            print("Thank you for playing this game !")
                            print("")
                        else:
                            print("Wrong >.< Try again !\n")
                            print("")

                        counter = counter + 1
                        print("")



            elif (option == 10): # email

                email = EmailMessage()
                email['from'] = str(input(("From: ")))
                email['to'] = ", ".join([i.email for i in lis])
                email['subject']= str(input("Subject: "))
                email.set_content(str(input("Message: ")))

                with smtplib.SMTP(host= 'smtp.gmail.com', port = 587) as smtp:
                    smtp.ehlo() #connection
                    smtp.starttls()# start security
                    smtp.login(str(input("Email: ")), str(input("Password: ")))
                    smtp.send_message(email)

                    print("MESSAGE SENT !\n")

                    print("")


            elif (option==11): # Exit
                swtich=False
                print("")

            else:
                print("You have entered wrong number please try again\n")
                print("")

 # main run
if __name__=='__main__':
    main()

