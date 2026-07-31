exchange_rate = 35.5

direction = input("เลือกทิศทางการแปลง (1 = THB to USD, 2 = USD to THB): ")
amount = float(input("กรุณาใส่จำนวนเงินที่ต้องการแปลง: "))

if direction == "1":
    result = amount / exchange_rate
    print(f"{amount} THB = {result:.2f} USD")
    print(f"สูตรคำนวณ: {amount} ÷ {exchange_rate} = {result:.2f}")
elif direction == "2":
    result = amount * exchange_rate
    print(f"{amount} USD = {result:.2f} THB")
    print(f"สูตรคำนวณ: {amount} × {exchange_rate} = {result:.2f}")
else:
    print("กรุณาเลือกทิศทางการแปลงที่ถูกต้อง (1 หรือ 2)")
