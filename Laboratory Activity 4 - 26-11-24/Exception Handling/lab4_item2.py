def main():
    try:
        size = int(input("Enter the size of the array: "))
        arr = [0.0] * size

        print("Enter the elements of the array:")
        for i in range(size):
            arr[i] = float(input())

        index = int(input("Enter the index of the element to print: "))

        print(f"Element at index {index}: {arr[index]:.2f}")
    
    except IndexError:
        print(f"Index {index} is invalid.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
