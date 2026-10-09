print("=== เครื่องคิดเลขอย่างปลอดภัย ===")

try:

    try:
        num1 = float(input("ตัวเลขที่ 1: "))
        num2 = float(input("ตัวเลขที่ 2: "))
    except ValueError:
        raise TypeError("กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")

    operator = input("เครื่องหมาย (+, -, *, /): ")

    if operator not in ["+", "-","*", "/"]:
        raise ValueError("เครื่องหมายไม่ถูกต้อง")


    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
        result = num1 / num2

    print("ผลลัพธ์:", result)

except TypeError as e:
    print("TypeError:", e)

except ValueError as e:
    print("ValueError:", e)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

finally:
    print("จบการทำงาน")