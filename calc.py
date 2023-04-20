def calc():
    print("1 - MULTI")
    print("2 - MINUS")
    print("3 - DIVINE")
    print("4 - PLUS")
    print("X - EXIT")
    return input("Your selection: ")

if __name__ == "__main__":
    while True:
        user_selection = calc().upper()
        if user_selection == "X":
            print("Exiting...")
            break
        elif str.isdigit(user_selection):
            num = int(user_selection)
            if num < 5:
                num1 = input("Please select a number: ")
                num2 = input("Please select a number: ")
                if num == 1:
                    print(f"{num1} * {num2} = {int(num1) * int(num2)}")
                elif num == 2:
                    print(f"{num1} - {num2} = {int(num1) - int(num2)}")
                elif num == 3:
                    if num2 == 0:
                        print("Error: Cannot divide by 0")
                    else:
                        print(f"{num1} / {num2} = {int(num1) / int(num2)}")
                elif num == 4:
                    print(f"{num1} + {num2} = {int(num1) + int(num2)}")
                else:
                    print("Invalid input")
        else:
            print("Invalid input")
