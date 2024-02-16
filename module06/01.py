# Work with files

# "r" - open for reading(default)
# "w" - open for writing truncing the files first
# "x" - creat a new file and open it for writing
# "a" - open for writing appending to the  end of the file if it exits
# "b" - binary mode
# "t" - text mode(default)


f = open("module06/data.txt", mode="w+")

f.seek(20)

print(f.read(10))

print(f.readlines())



f.close()
