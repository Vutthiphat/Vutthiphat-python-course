weight = float(input("Enter Your Weight : "))
height = float(input("Enter Your Height :"))

bmi = weight/(height**2)
print("BMI : ",bmi)

if bmi <= 18.5 :
    print("Underweight")
elif bmi >= 18.6 :
    print("Normal weight")
elif bmi >= 25.0 :
    print("Overweight")
elif bmi >= 30 :
    print("obese")
