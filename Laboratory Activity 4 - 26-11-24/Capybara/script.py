from Capybara import Capybara

def main():
    capybara1 = Capybara("Biscoff", "M", 5)

    capybara_list = [capybara1]

    try:
        test_case_number = int(input("Enter the test case number: "))
        if test_case_number == 1:
            selected_capybara = capybara_list[0]
            print(f"Test Case {test_case_number}: Name: {selected_capybara.name}, "
                  f"Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
        else:
            print("Invalid test case number. Please select 1.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()