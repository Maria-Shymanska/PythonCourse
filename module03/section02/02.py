# Write a amount_payment function that takes a list of payments as input,
# sums up the positive values, and returns the payment amount at the end of the month.


def amount_payment(payment):

    total_payment = 0

    for amount in payment:
        if amount > 0:
            total_payment += amount

    return total_payment


# Write a prepare_data function that removes the top and lowest values
# from the passed list,sorts it in ascending order,
# and returns the modified list as a result.


def prepare_data(data):
    max_value = max(data)
    min_value = min(data)
    # Remove max and min values from the data list
    data.remove(max_value)
    data.remove(min_value)

    # Sort the modified data list
    sorted_data = sorted(data)

    return sorted_data


# As we know, a key in a dictionary must be unique, while its meaning is not.
# Implement the lookup_key function to search for all keys by value in the dictionary. With the first parameter,
# we pass the dictionary to the function, and with the second parameter, we pass the value we want to find.
# Thus, the result can be either a list of keys or an empty list if we don't find anything.

# def lookup_key(data, value):

#     keys = [ ]
