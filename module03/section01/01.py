def print_even_squares(start, end, step=1):  # signature
    count = 1

    for i in range(start, end, step=1):
        if i % 2 == 0:
            print(f"{count} : {i} : {i ** 2}")
            count += 1

            print_even_squares(1, 10)


print_even_squares(
    10,
    start=1,
)
print_even_squares(1, start=10)  # not named params first
