# =========== Encoding Files =========== #

# When you run the unencoded example you will notice that the output displays strange characters.
# This can be fixed by specifying the encoding scheme, UTF-8 or UTF-8-SIG, as an additional arugment to the open() function. 
# utf-8-sig is a variation of the utf-8 encoding that includes a Byte Order Mark (BOM) at the beginning of the file.
# The BOM is a special marker that indicates the file is UTF-8 encoded.
# By using utf-8-sig, you can avoid the appearance of strange characters at the beginning of the text, as the BOM is properly handled.
# When you run the encoded example, using utf-8-sig, you will notice that the data is transformed so that it is compatible for reading.


# Unencoded example
print("\n--Unencoded Example--\n")

with open('example.txt', 'r') as file:
    lines = file.readlines() 
print(lines)


# Encoded example using utf-8
print("\n--Encoded Example using utf-8--\n")

with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines() 
print(lines) # do you see the BOM at the beginning of the file?


# Encoded example using utf-8-sig
print("\n--Encoded Example using utf-8-sig--\n")

with open('example.txt', 'r', encoding='utf-8-sig') as file:
    lines = file.readlines() 
print(lines)






 

