import random

# Generate a random two-digit lottery number
lottery_number = random.randint(10, 99)

# Prompt the user to enter a two-digit number
user_input = int(input("Enter a two-digit number (e.g., 45): "))

# Extract the individual digits of the lottery number and user input
lottery_digit1 = lottery_number // 10
lottery_digit2 = lottery_number % 10
user_digit1 = user_input // 10
user_digit2 = user_input % 10

# Check the winning conditions
if user_input == lottery_number:
    award = 10000
elif (user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2) and (user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2):
    award = 3000
elif (user_digit1 == lottery_digit1 or user_digit1 == lottery_digit2) or (user_digit2 == lottery_digit1 or user_digit2 == lottery_digit2):
    award = 1000
else:
    award = 0

# Display the lottery number and the user's award
print(f"The lottery number is {lottery_number}")
if award > 0:
    print(f"Congratulations! You win ${award}")
else:
    print("Sorry, you didn't win this time.")
