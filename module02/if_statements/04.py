a = int(input("Enter a number >>>"))


if (a > 0 and a < 10) or a % 2 == 1:
    print("number is positive")
else:
    print("None")

    # using if else for Validation

    name = input("Enter your name:")
    email = input("Enter your email address:")
    password = input("Enter your password:")

    if name == "":
        print("Name cannot be emty")
    else:
        if "@" not in email:
            print("invalid email address")
        else:
            if len(password) > 8:
                print("Password must be at least 8 characters long.")
            else:
                print("Registration successful.")
