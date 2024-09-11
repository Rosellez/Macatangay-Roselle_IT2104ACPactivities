def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = [char for char in input_string if char in vowels]
    return result

input_string = input("Enter a string: ")
vowel_list = find_vowels(input_string)
print("Vowels in the string:", vowel_list)
