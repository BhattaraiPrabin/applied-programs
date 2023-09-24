"""
unway International University has Account, Administration, IT and others 
department. In each department more than 5 staff are working. Account department 
on releases of the salary payment of staff, they calculated the tax of each staff. Below two 
tables are tax slab table approved by the government and Accounts department while the 
release of salary of staff they calculated each income tax for each staff.
If staff is individual, then as per first table income tax are calculated and if staff is 
married then as per second table income tax are calculated and deducted the income tax
amount on the basic salary of staffs and provided the monthly salary. Develop an Income 
Tax Software for Sunway International University, so that Account division should able 
to calculate the income tax of each employee through the system. System should ask for 
5 staff information at each time and based on data information provided as below sample; 
system will calculate the income tax and display the monthly salary based on the income 
tax.
Individual/Natural Person
Annual Income Income Tax Rate (FY 2021/22)
Up to Rs. 4,00,000 1%
Additional Rs. 1,00,000 10%
Additional Rs 2,00,000 20%
Additional Rs 6,00,000 30%
Additional Tax Above Rs 2,000,000 36%
Married/Couple:
Annual Income Income Tax Rate (FY 2021/22)
Up to Rs. 4,50,000 1%
Additional Rs. 1,00,000 10%
Additional Rs 2,00,000 20%
Additional Rs 5,50,000 30%
Additional Tax Above Rs 2,000,000 36%
Design your program according to the screen interaction given below.
[INPUT]
Please enter the number of staff you wanted you provide data: 5
Enter for the 1 Staff Information:
Enter Staff Name [1]:Kamal Sharma
Enter Address [1]: Bhakatapur
Enter Pan No [1]: 927867986
Enter ‘Y’ for Married and ‘N’ for Unmarried Status [1]: Y
Enter FY [1]:2021/22
Enter Staff per month income [Rs.][1]:36540
Enter for the 2 :
Enter Staff Name [2]: Prakash Shrestha
Enter Address [2]: Kathmandu
Enter Pan No [2]:2345678
Enter ‘Y’ for Married and ‘N’ for Unmarried Status [2]:N
Enter FY [2]:2021/22
Enter Staff per month income [Rs.][2]:35000
CSC3532/Sept/Oct2022 Page 5 of 5
[Output]
Sunway International University Account Department----Line 1 
MaitiDevi, Kathmandu-------------------Line 2
Welcome to-------------------------------Line 3
Salary& Tax Calculate System (STCS) Line 4
Staff Name: Kamal Sharma Address: Bhakatapur
PAN No: 927867986 FY: 2021/22 Married Status=Y
Staff Kamal Sharma with PAN 927867986 fall under 1% Tax salb.
Kamal Sharma (PAN 927867986) to pay tax to government is [Rs.]= 
4500
Sunway International University Account Department 
MaitiDevi, Kathmandu 
Welcome to
Salary& Tax Calculate System (STCS)
Staff: Prakash Shrestha Address: Kathmandu
PAN No: 2345678 FY: 2021/22 Married Status=N
Staff Prakash Shrestha with PAN 2345678 fall under 1% Tax salb.
Prakash Shrestha (PAN 2345678) to pay tax to government is [Rs.]= 
4500
Note: Your program should include the following
1. Define all related variables.
2. Staff_No named list must be assigned holding total number of staff.
3. Use looping and function to receive data.
4. Input function with names Staff_Info, calculation tax function with names 
Calculate_Tax_Of_Staff holds staff married status as single parameter 
information 
and inside that function two function with named 
Calculate_Tax_Of_Staff_Married and 
Calculate_Tax_Of_Staff_Unmarried called based on the married status 
of the Staff.
5. if the flag is on then Calculate_Tax_Of_Staff_Married function call; this 
function must provide all the calculation of the Staff with married status 
6. if the flag is off then Calculate_Tax_Of_Staff_Unmarried function call; this 
function must provide all the calculation of the Staff with unmarried status
7. Display_Staff_Info display the Staff information.
8. Display_Static_Info function must hold the content information of Line 1 to 4 
must. Also for static information i.e. Line1 to Line 4 program must be write in a file name 
student name as txt format with append mode.
9. Staff_Info function should contain Staff information and students must provide 
their name as input. Based on the married status; status flag as parameter must be 
passed to the Calculate_Tax_Of_Staff function.
10. Output section should be write to a file name staff.txt with same as console 
output (Output_File_Write function)

"""


def Staff_Info():
    Staff_No = []
    staff_number = int(
        input("Please enter the number of staff you wanted you provide data: "))
    for i in range(staff_number):
        Staff = []
        print(f" Enter for the {i+1} Staff Information:")
        name = input(f"Enter Staff Name [{i+1}]: ")
        address = input(f"Enter Address[{i+1}]: ")
        pan = input(f"Enter Pan Number[{i+1}]: ")
        status = input(
        f"Enter ‘Y’ for Married and ‘N’ for Unmarried Status [{i+1}]:  ")
        fy = input(f"Enter FY [{i+1}]: ")
        income = float(input(f"Enter Staff per month income [Rs.] [{i+1}]: "))
        Staff.append(name)
        Staff.append(address)
        Staff.append(pan)
        Staff.append(status)
        Staff.append(fy)
        Staff.append(income)
        Staff_No.append(Staff)
    return Staff_No, staff_number


def Calculate_Tax_Of_Staff_Married(income):
    if income <= 450000:
        tax_per = 1
        total_tax_amount = ((income*tax_per)/100)

    elif income > 450000 and income <= 450000+100000:
        tax_per = 10
        total_tax_amount = ((450000*1)/100)+(((income-450000)*tax_per)/100)

    elif income > 450000+100000 and income <= 450000+100000+200000:
        tax_per = 20
        total_tax_amount = ((450000*1)/100)+((100000*10)/100) + \
            (((income-(450000+100000))*tax_per)/100)

    elif income > 450000+100000+200000 and income <= 450000+100000+200000+550000:
        tax_per = 30
        total_tax_amount = ((450000*1)/100)+((100000*10)/100) + \
            (((200000)*20)/100)+(((income-(450000+100000+200000))*tax_per)/100)

    else:
        tax_per = 36
        total_tax_amount = ((450000*1)/100)+((100000*10)/100)+(((200000)*20)/100)+(
            ((550000)*30)/100)+(((income-(450000+100000+200000+550000))*tax_per)/100)

    return tax_per, total_tax_amount


def Calculate_Tax_Of_Staff_Unmarried(income):
    if income <= 400000:
        tax_per = 1
        total_tax_amount = ((income*tax_per)/100)

    elif income > 400000 and income <= 400000+100000:
        tax_per = 10
        total_tax_amount = ((400000*1)/100)+(((income-400000)*tax_per)/100)

    elif income > 400000+100000 and income <= 400000+100000+200000:
        tax_per = 20
        total_tax_amount = ((400000*1)/100)+((100000*10)/100) + \
            (((income-(400000+100000))*tax_per)/100)

    elif income > 400000+100000+200000 and income <= 400000+100000+200000+6000000:
        tax_per = 30
        total_tax_amount = ((400000*1)/100)+((100000*10)/100) + \
            (((200000)*20)/100)+(((income-(400000+100000+200000))*tax_per)/100)

    else:
        tax_per = 36
        total_tax_amount = ((400000*1)/100)+((100000*10)/100)+(((200000)*20)/100)+(
            ((600000)*30)/100)+(((income-(400000+100000+200000+600000))*tax_per)/100)

    return tax_per, total_tax_amount


def Calculate_Tax_Of_Staff(status, income):
    if status == 'y' or status == 'Y':
        tax_per, total_tax_amount = Calculate_Tax_Of_Staff_Married(income)

    elif status == 'n' or status == 'N':
        tax_per, total_tax_amount = Calculate_Tax_Of_Staff_Unmarried(income)
    else:
        print("Invalid Input : ")
        exit()
    return tax_per, total_tax_amount


def Display_Staff_Info(name, address, pan, status, fy, tax_per, total_tax_amount):
    staff = f""" 
Staff: {name}                        Address: {address}
PAN No: {pan}         FY: {fy}       Married Status={status}
          
Staff {name} with PAN {pan} fall under {tax_per}% Tax salb.
{name} (PAN {pan}) to pay tax to government is [Rs.]= {total_tax_amount}
          """
    print(staff)
    with open("staff.txt", 'a') as f:
        f.write(staff)


def Display_Static_Info():
    heading = """       
Sunway International University Account Department 
             MaitiDevi, Kathmandu 
                Welcome to
        Salary& Tax Calculate System (STCS)
"""
    print(heading)
    with open("1.txt", 'a') as f:
        f.write(heading)


if __name__ == "__main__":
    Staff_No, staff_number = Staff_Info()
    for i in range(staff_number):
        tax_per, total_tax_amount = Calculate_Tax_Of_Staff(
            Staff_No[i][3], Staff_No[i][5])
        Display_Static_Info()
        Display_Staff_Info(Staff_No[i][0], Staff_No[i][1], Staff_No[i]
                           [2], Staff_No[i][3], Staff_No[i][4], tax_per, total_tax_amount)      
