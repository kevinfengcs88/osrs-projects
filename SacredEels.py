def option1(num):
    price = int(input("Enter the current price of Zulrah's scales: "))
    return ("Gp/hr: " + str(num * 7.5 * price))

def option2(afk):
    if afk == 1:
        num = 220
    elif afk == 2:
        num = 200
    else:
        num = 180
    price = int(input("Enter the current price of Zulrah's scales: "))
    return ("Gp/hr: " + str(num * 7.5 * price))

option = input("Would you like to: \n(a) Enter the number of eels per hour\n(b) Enter a degree of AFK")
option.lower()

while option != "a" or option != "b":
    if option == "a" or option == "b":
        break
    option = input("Would you like to: \n(a) Enter the number of eels per hour\n(b) Enter a degree of AFK")

if option == "a":
    try:
        eels = int(input("Enter the number of eels per hour: "))
    except ValueError:
        print("Please rerun the program and enter an integer: ")
    print(option1(eels))
else:
    awayFromKeyboard = int(input("Enter a number from 1-3, with 1 being the least, and 3 being the most, of how AFK you will fish: "))
    while awayFromKeyboard < 1 or awayFromKeyboard > 3:
        try:
            awayFromKeyboard = int(input("Enter a number from 1-3, with 1 being the least, and 3 being the most, of how AFK you will fish: "))
        except ValueError:
            awayFromKeyboard = int(input(("Please enter an integer between 1 and 3 inclusive: ")))
    print(option2(awayFromKeyboard))
