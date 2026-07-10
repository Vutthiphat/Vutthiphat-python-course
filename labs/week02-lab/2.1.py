print("1. circle calculator :")
print("   -Ask user for radius")
print("   -Calculate circumference(2 * π * r)")
print("   -Use 3.14159 for π")
print("_"*50)
print()
#input
redius = float(input("Redius : "))
#process
area = 3.14159 *redius ** 2
circumference = 2 * 3.14159 * redius
#output
print(f"Area of this Circle : {area}") #{area: .2f} การ Fix ให้ออกมาเเค่ทศนิยม 2 ตำเเหน่ง
print(f"Circumference of this Circle : {circumference}")

print("_" * 50)
print()

