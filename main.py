import BMI
import retirement


def main():
    print("What feature do you want to use?")
    print("1. BMI")
    print("2. Retirement")
    choice = input("Choose: ")
    while choice != "1" or choice != "2":
        choice = input("Choose: ")

    if choice == "1":
        weight = input("Enter weight:")
        feet = input("Enter feet:")
        inches = input("Enter Inches:")
        int_weight = int(weight)
        int_feet = int(feet)
        int_inches = int(inches)


        s = BMI.BMI(weight,feet,inches)
        value = s.BMI_calculator(int_weight, int_feet, int_inches)
        print(value)

        status = s.BMI_category(value)
        print(status)

    if choice == "2":
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        percentage_saved = input("Enter Percentage of salary Saved: ")
        goal = input("Retirement goal: ")
        int_age = int(age)
        int_salary = int(salary)
        int_percent = int(percentage_saved)
        int_goal = int(goal)

        t = retirement.retirement(int_age,int_salary,int_percent, int_goal)
        yearly_savings = t.annual_savings(int_salary, int_percent)
        goal = t.retirement_calculator(yearly_savings, int_age, int_goal)


main()