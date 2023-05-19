def is_symmetrical(string):
    length=len(string)
    for i in range(length//2):
        if string[i] != string[length-i-1]:
            return False
        return True

def is_palindrome(string):
    return string == string[::-1]
input_string=input('Enter a string:')

if is_symmetrical(input_string):
    print("The string is a symmetrical.")
else:
    print("The string is not a symmetrical.")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")