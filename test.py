import BMI
import retirement


def test_BMI_calculator():
    assert BMI.BMI.BMI_calculator(0, 125, 5, 3) == 22.7


def test_BMI_status():
    assert BMI.BMI.BMI_category(0, 23) == "NormalWeight"
    assert BMI.BMI.BMI_category(0, 5) == "Underweight"
    assert BMI.BMI.BMI_category(0, 27) == "OverWeight"
    assert BMI.BMI.BMI_category(0, 50) == "Obese"


def test_retirement_savings():
    assert retirement.retirement.annual_savings(0, 50000, 20) == 13500


##def test_goalMet():
   ## assert retirement.retirement.retirement_calculator
