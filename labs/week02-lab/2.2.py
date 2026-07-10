print("4. BMI Calculator : ")
print(" -Ask for weight (kg) and height (m)")
print(" -Calculate: BMI = weight / (height ** 2)")
print("_"*50)
ptint()

#input
weight = float(input("Enter your Weight (kg):"))
height = float(input("Enter your Height (M):"))

#process
BMI = weight / (height ** 2)

#output
print(f"Your BMI is {BMI:.2f}.")