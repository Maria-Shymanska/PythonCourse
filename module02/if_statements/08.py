#  Implement the execution control operator so that it sets the logical variable
#  is_next to True if the number of points scored is greater than or equal to 83.
#  Otherwise, the value of the variable is False.


is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False

    # Casting to Boolean type

is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")


is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)

# There is a variable work_experience that determines the length of service of a programmer.
# Depending on the length of service, assign the variable developer_type the value "Junior", "Middle" or "Senior". Use,
# if necessary, the Boolean operators or and and during checks.


work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 1:
    developer_type = "Junior"
elif 1 < work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"

    # A string is an iterable object, which means we can use it in a for loop.
    # Count the number of occurrences of a character from the search variable in a given message line.
    # Place the result in the result variable.

    message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0

for char in message:
    if char == search:
        result += 1

print("Кількість входжень символу", search, "у рядок:", result)


# operator break

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum = sum + i

        # The situation is simple, you need to calculate the number of SMS that need to be sent in one mailing package to potential buyers.
        # A total of 1000 paid SMS are allocated per day for the marketing campaign pool=1000.
        # A member of the marketing department enters the number of mailings quantity, and you calculate the batch size chunk = pool // quantity.
        # Work out the division by zero error.

        pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print("Divide by zero completed!")
