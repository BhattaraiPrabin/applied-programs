# Write a program to create a list of 5 numbers (input from user) and write that list in a file
# “listdata.txt”



def input_number():
    num = []
    for i in range(5):
        try:
            num1 = float(input("enter number: "))
            num.append(num1)
        except:
            print("invalid input")
            return None
    return num

def write_in_file(file, nums):
    with open(file, "w") as f:
        f.write(str(nums))

def main():
    num = input_number()
    file = "listdata_1.txt"
    if num is not None:
        write_in_file(file, num)

main()