filename = input("Enter filename to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")