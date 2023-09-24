# Function to get a list of 5 numbers from the user
def get_numbers():
    numbers = []
    for i in range(5):
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

# Function to write a list of numbers to a file
def write_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + '\n')

# Function to read numbers from a file and write even numbers to another file
def filter_even_numbers(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            for line in input_file:
                num = int(line.strip())
                if num % 2 == 0:
                    output_file.write(str(num) + '\n')
        print(f"Even numbers from '{input_filename}' have been written to '{output_filename}'.")
    except FileNotFoundError:
        print("File not found. Make sure 'data.txt' exists.")

# Main program
if __name__ == "__main__":
    numbers = get_numbers()
    write_to_file("data.txt", numbers)
    filter_even_numbers("data.txt", "dest.txt")
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\