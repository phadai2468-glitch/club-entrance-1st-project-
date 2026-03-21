try:
    num = int(input("Enter the pin: "))
    if num < 1000:
        print("write the full pin")
    elif num > 9999:
        print("your pin must consist of only 4 digits")
    else:
        print("pin accepted")
        input("your password is saved, press Enter to continue...")

except ValueError:
    print("try a valid number")