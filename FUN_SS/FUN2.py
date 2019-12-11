from FUN_SS.FUN import Profile
from PIL import Image
import random
import smtplib
from email.message import EmailMessage


def main():
    id= 0
    lis=[]
    swtich = True
    print("Welcome to my program !")
    print("--------------------------------------------")
    while(swtich):
        print("Enter one of the following options: ")
        print("1. Add profile")
        print("2. Display profile")
        print("3. Search for a profile")
        print("4. Remove profile")
        print("5. Remove All")
        print("6. Pictures")
        print("7. Resize pictures")
        print("8. Random number game")
        print("9. Sending Email for all profiles")
        print("10. Exit")
        option=  int(input("Your options: "))

        if (option == 1): # add into the list
            id= id+1
            lis.append(Profile(id, str(input("Enter your first name: ")),str(input("Enter your last name: ")),
                         int(input("Enter your age: ")), str(input("Enter your email without writing @gmail.com: "))+"@gmail.com", str(input("Enter your hobby: "))))


        elif(option==2): # print the list
            for obj in lis:
                print("--------------------------------------------")
                print(f"ID: {obj.id}")
                print(f"First Name: {obj.fname}")
                print(f"Last Name: {obj.lname}")
                print(f"Age: {obj.age}")
                print(f"Email: {obj.email}")
                print(f"Hobby: {obj.hobby}")
                print("--------------------------------------------")
        elif(option == 3): # search for an object in the list
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
        elif(option==4): # remove an object from the list
            enter= int(input("Enter the ID you want to delete the list: "))
            for obj in lis:
                if (enter==obj.id):
                    lis.remove(obj)

        elif(option==5): # clear the list
            lis.clear()

        elif (option == 6): # image opening
            print("Enter one of the following Images you want to display: ")
            print("1. Irelia")
            print("2. Irelia Mirror")
            print("3. IG Irelia")
            print("4. Exit")
            option2 = int(input("Your option: "))
            if(option2 == 1):
                ima = Image.open('Screen Shot 1441-03-13 at 3.10.09 PM copy.png')
                ima.show()

            elif(option2 == 2):
                ima2 = Image.open('157338784156073568 copy.png')
                ima2.show()

            elif(option2 == 3):
                ima3 = Image.open('Screen Shot 1441-01-28 at 3.03.54 PM copy.png')
                ima3.show()

            elif(option2 == 4):
                continue

            else:
                print("You have entered wrong number please try again")


        elif (option == 7): # image resizing with thumbnailing
            print("Enter one of the following Images you want to display: ")
            print("1. Resize Irelia")
            print("2. Resize  Irelia Mirror")
            print("3. Resize  IG Irelia")
            print("4. Exit")
            option3 = int(input("Your option: "))

            if (option3 == 1):
                imag = Image.open('Screen Shot 1441-03-13 at 3.10.09 PM copy.png')
                he = int(input("Enter height: "))
                wi = int(input("Enter Width: "))
                imag.thumbnail((he, wi))
                imag.save(str(input("Enter the file name you want to save: " )) + ".png")
                imag.show()

            elif (option3 == 2):
                imag2 = Image.open('157338784156073568 copy.png')
                he2 = int(input("Enter height: "))
                wi2 = int(input("Enter Width: "))
                imag2.thumbnail((he2, wi2))
                imag2.save(str(input("Enter the file name you want to save: " )) + ".png")
                imag2.show()
            elif (option3 == 3):
                imag3 = Image.open('Screen Shot 1441-01-28 at 3.03.54 PM copy.png')
                he3 = int(input("Enter height: "))
                wi3 = int(input("Enter Width: "))
                imag3.thumbnail((he3, wi3))
                imag3.save(str(input("Enter the file name you want to save: " )) + ".png")
                imag3.show()
            elif (option3 == 4):
                continue
            else:
                print("You have entered wrong number please try again")

        elif (option == 8): # random game
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
            if(option4 == 1):


                while(switch2): # 1 - 10 game
                    random_number = int(random.randint(1, 10))

                    enter=int(input(("Enter numbers from 1-10: ")))
                    print("")
                    if(enter == random_number):
                        print(f"WOOO You won it with record {counter} times\n")
                        switch2= False
                    elif(enter == 0):
                        switch2 = False
                        print("Thank you for playing this game !")
                    else:
                        print("Wrong >.< Try again !\n")

                    counter = counter +1


            elif (option4 == 2): # 1 - 50 game

                while (switch2):
                    random_number = int(random.randint(1, 50))

                    enter2 = int(input(("Enter numbers from 1-50: ")))
                    print("")
                    if (enter2 == random_number):
                        print(f"WOOO You won it with record {counter} times\n")
                        switch2 = False
                    elif (enter2 == 0):
                        switch2 = False
                        print("Thank you for playing this game !")
                    else:
                        print("Wrong >.< Try again !\n")

                    counter = counter + 1


            elif (option4 == 3): # 1 - 100 game

                while (switch2):
                    random_number = int(random.randint(1, 100))

                    enter3 = int(input(("Enter numbers from 1-50: ")))
                    print("")
                    if (enter3 == random_number):
                        print(f"WOOO You won it with record {counter} times\n")
                        switch2 = False
                    elif (enter3 == 0):
                        switch2 = False
                        print("Thank you for playing this game !")
                    else:
                        print("Wrong >.< Try again !\n")

                    counter = counter + 1



        elif (option == 9): # email

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


        elif (option==10): # Exit
            swtich=False

        else:
            print("You have entered wrong number please try again\n")

 # main run
if __name__=='__main__':
    main()

