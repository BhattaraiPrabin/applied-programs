def categorize_temperature(temp):
    if temp > 85:
        return "very hot"
    elif 60 <= temp <= 85:
        return "pleasant day"
    else:
        return "very cold"

def main():
    num_days = int(input("How many days to record: "))
    temperatures = []

    for day in range(1, num_days + 1):
        temperature = float(input(f"Temperature day [{day}]= "))
        temperatures.append(temperature)

    total_temperature = sum(temperatures)
    average_temperature = total_temperature / num_days

    hot_days = 0
    pleasant_days = 0
    cold_days = 0

    print("\nDaily Temperature Report")
    for day, temp in enumerate(temperatures, 1):
        category = categorize_temperature(temp)
        print(f"Temperature day [{day}]={temp} Celsius {category}")
        if category == "very hot":
            hot_days += 1
        elif category == "pleasant day":
            pleasant_days += 1
        else:
            cold_days += 1

    print(f"The average Temp for {num_days} days={average_temperature:.2f} Celsius")
    print(f"Number of hot days ={hot_days} day/s")
    print(f"Number of pleasant days ={pleasant_days} day/s")
    print(f"Number of cold days ={cold_days} day/s")

if __name__ == "__main__":
    main()
