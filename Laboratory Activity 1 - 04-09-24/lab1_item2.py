char1, char2 = input("Enter two space-separated characters: ").split()

larger_char = max(char1, char2)

print("----------------------------------------")
print("The character with the greater value is:", larger_char)
print("----------------------------------------")
asciiVal1 = ord(char1)
asciiVal2 = ord(char2)
print("This part is optional to include.")
print("Showing ASCII Values: ")
print(f"{char1} : {asciiVal1}")
print(f"{char2} : {asciiVal2}")
