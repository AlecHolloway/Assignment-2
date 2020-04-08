class BMI:
    def __init__(self, weight, feet, inches):
        self.weight = weight
        self.feet = feet
        self.inches = inches


    def BMI_calculator(self, weight, feet, inches):
        weight_kg = float(weight) * 0.45
        feet_to_inches = feet * 12
        height_inches = float((feet_to_inches + inches)) * 0.025
        BMI_value = weight_kg / (height_inches * height_inches)
        return round(BMI_value, 1)

    def BMI_category(self, BMI_value):
        if BMI_value < 18.5:
            status = "Underweight"
        elif BMI_value >= 18.5 and BMI_value <= 24.9:
            status = "NormalWeight"
        elif BMI_value >= 25 and BMI_value <= 29.9:
            status = "OverWeight"
        elif BMI_value >= 30:
            status = "Obese"
        return status
