import csv

csv = open("Info.csv", "w")

first_name = ""
last_name = ""
city = ""
postal_code = ""
credit_card = ""

def printMenu():
    while True:
        print("1. Enter Customer Information")  
        print("2. View Customer Information. Note: You can only view information if you have previously entered information.")
        print("3. Exit")
        choice = int(input("Please select an option (1, 2, or 3): "))
        if choice == 1:
            enter_customer_information()
            validateCreditCard()
            validatePostalCode()
            csv.write("first name, " + first_name + "\n")
            csv.writelines("last name, " + last_name + "\n")
            csv.writelines("city, " + city + "\n")
            csv.writelines("postal code, " + postal_code + "\n")
            csv.writelines("credit card, " + credit_card + "\n")
        elif choice == 2:
            generateCustomerDataFile()
        elif choice == 3:
            print("You have now exited the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def validatePostalCode():
    global postal_code
    verified_postal_code = False
    while not verified_postal_code:
        postal_code = input("Enter your postal code: ")
        with open("Postal_Codes.txt", "r") as file_2:
            if len(postal_code) == 3 and postal_code in file_2.read():
                print("Valid postal code.")  
                verified_postal_code = True
            else:
                print("Invalid postal code. Please try again.")

def validateCreditCard():
    verefied_credit_card = False
    odd = 0
    even = 0
    counter = 0
    
    while verefied_credit_card == False:
        global credit_card
        credit_card = input("Enter your credit card number: ")
        credit_card = credit_card.replace(" ", "")
        credit_card_digits = [digit for digit in str(credit_card)]
        credit_card_digits_2 = credit_card_digits [::-1]
        for digits in credit_card_digits_2:
            if len(credit_card_digits_2) < 9:
                print("Invalid credit card number. Please try a different one.")
            else:
                if counter % 2 == 0:
                    str(digits) == int(digits)
                    odd = str(odd) + str(digits)
                    counter = counter + 1
                else:
                    digits = int(digits)
                    even == digits * 2
                    if int(even) <= 9:
                        even = str(even) + str(digits)
                    if int(even) > 10:
                        even = str(even)
                        for values in even:
                            values = int(values)
                            digits = values
                            even_2 = str(digits) + even
                    counter = counter + 1 
                    total = str(even) + str(odd)
                    total_2 = int(total) % 10
                    if total_2 == 0:
                        print("Valid credit card.")
                        verefied_credit_card = True
                    else:
                        print("Invalid credit card. Please try a different one.") 
def enter_customer_information():
    global first_name, last_name, city
    print("\nEnter Customer Information")
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    city = input("Enter the city you live in: ")

    customer_data = {
        "first name": first_name,
        "last name": last_name,
        "city": city,
        "credit card" : credit_card,
        "postal code" : postal_code
        
    }

    print("\nCustomer Information Saved:")
    print(f"Name: {customer_data['first name']}")
    print(f"Last name: {customer_data['last name']}")
    print(f"City: {customer_data['city']}")

def generateCustomerDataFile():
   file = open("Info.csv", "r")
   print("Customer data is now available at " + str(file))

if __name__ == "__main__":
    printMenu()
csv.close()
