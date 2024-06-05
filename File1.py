import random

s_letter = "abcdefghijklmnopqrstuvwxyz"
b_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "%@\\₹&/"


def create_banner():
    banner = f"""
    ******************************
    *                            *
    *                            *
    *    Password Generator      *
    *                            *
    *                            *
    ******************************
    """
    return banner


def type_selection():
    print(create_banner())
    passWordS = int(input("Number of passwords: "))
    print("[1] Only numbers")
    print("[2] Numbers and letters")
    print("[3] Numbers, letters, and capital letters")
    print("[4] Numbers, symbols, letters, and capital letters")
    X = int(input("Select the option: "))

    if X not in [1, 2, 3, 4]:
        print("Invalid option selected... Exiting.")
        exit()

    if X == 1:
        use = numbers
    elif X == 2:
        use = s_letter + numbers
    elif X == 3:
        use = b_letter + numbers + s_letter
    elif X == 4:
        use = b_letter + numbers + s_letter + symbols

    create_pass(passWordS, use)


def create_pass(passWordS, use):
    File_name = input("Set the file name: ")
    length_for_pass = int(input(f"Custom password length for password: "))
    i = 0
    while i < passWordS:
        password = "".join(random.sample(use, length_for_pass))
        # Save each password in a separate file
        with open(f"{File_name}.txt", "a") as fo:
            fo.write(password + "\n")
            print(password)
        i += 1


if __name__ == "__main__":
    type_selection()
    print("Password generation completed...")
    exit()
