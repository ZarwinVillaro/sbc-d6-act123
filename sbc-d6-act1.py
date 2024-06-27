userad = input("Enter a word to check: ")
userad = userad.lower().replace("", "")

palindrome = ""

for i in userad:
    palindrome = i + palindrome

if palindrome == userad:
    print("This is palindrome")

else:
    print("This is not palindrome")