def is_palindrome(number):
    num_str = str(number)
    
    if num_str == num_str[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

number = int(input("Enter an integer: "))
result = is_palindrome(number)
print(result)
