def convert_camel_to_snake(text):
    # void
    # CrazyFrogSound >= crazy_frog_sound
    # iterate

    j = 0
    res = ""
    for char in text:
        if char.isupper():
            if j == 0:
                res += char.lower()
            else:
                char += "_" + char.lower
        else:
            res += char
            j += 1

            return res

        s = "CrazyFrogSound"

        New_title = convert_camel_to_snake(s)

        print(New_title)
