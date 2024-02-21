"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)


encoding: Windows, ASCII, UTF-16
UTF-8 is the dominant encoding for the World Wide Web (and internet technologies), 
accounting for 98.2% of all web pages, 99.0% of the top 10,000 pages, and up to 100% for many languages, 
as of 2024.[9] Virtually all countries and languages have 95% or more use of UTF-8 encodings on the web.

"""

f = open("module06/data.txt", mode="w+")
f.seek(20)
print(f.read(10))
print(f.readlines())
f.close()