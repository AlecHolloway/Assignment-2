class retirement:
    def __init__(self, age, salary, percentage_saved, retirement_goal):
        self.savings = 0
        self.age = age
        self.salary = salary
        self.percentage_saved = percentage_saved
        self.retirement_goal = retirement_goal


    def annual_savings(self, salary, percentage_saved):
        percentage_saved = percentage_saved / 100
        employee_match = (salary * percentage_saved) * 0.35
        annual_savings = (salary * percentage_saved) + employee_match
        ##self.retirement_calculator(annual_savings, self.age, self.retirement_goal)
        return annual_savings

    def retirement_calculator(self, annual_savings, age, retirement_goal):
        while age <= 100:
            if self.savings < retirement_goal:
                self.savings += annual_savings
                self.goal_met = False
            elif self.savings >= retirement_goal:
                print("You have reached your retirement goal at age ", age)
                self.goal_met = True
                break
            age = age + 1
        if self.goal_met == False:
            print("You did not meet your goal. Amount in savings is ", self.savings)
        return self.goal_met

