# # to add one element in the end of the list method append

fruit_list = ["apple", "orange", "banana", "pear"]

fruit_list.append("pomegranate")

print(fruit_list)


# Implement the lookup_key function to search for all keys by value in the dictionary.
# With the first parameter, we pass the dictionary to the function,
# and with the second parameter, we pass the value we want to find.
# Thus, the result can be either a list of keys or an empty list if we don't find anything.


def lookup_key(data, value):
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys


print(lookup_key({"key1": 1, "key2": 2, "key3": 3, "key4": 2}, 2))
