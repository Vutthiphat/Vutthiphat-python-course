def calculate_electricity_cost(units):
    cost_1_50 = 0.0
    cost_51_100 = 0.0
    cost_101_200 = 0.0
    cost_over_200 = 0.0
    service_fee = 25.0

    # คำนวณแบบก้าวหน้าตามช่วงหน่วย
    if units > 200:
        cost_over_200 = (units - 200) * 4.50  # สมมติเรทส่วนเกิน 200 หน่วย = 4.50 บาท
        cost_101_200 = 100 * 4.00             # ช่วง 101-200 (100 หน่วย)
        cost_51_100 = 50 * 3.00               # ช่วง 51-100 (50 หน่วย)
        cost_1_50 = 50 * 2.50                 # ช่วง 1-50 (50 หน่วย)
    elif units > 100:
        cost_101_200 = (units - 100) * 4.00
        cost_51_100 = 50 * 3.00
        cost_1_50 = 50 * 2.50
    elif units > 50:
        cost_51_100 = (units - 50) * 3.00
        cost_1_50 = 50 * 2.50
    else:
        cost_1_50 = units * 2.50

    total = cost_1_50 + cost_51_100 + cost_101_200 + cost_over_200 + service_fee
    return cost_1_50, cost_51_100, cost_101_200, cost_over_200, service_fee, total


# ส่วนการทำงานของเมนู (อยู่นอกฟังก์ชัน)
while True:
    print("\n==== โปรแกรมคำนวณไฟฟ้า ====")
    print("1. คำนวณไฟฟ้า")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู (1/2): ")

    if choice == "1":
        units = float(input("กรอกจำนวนหน่วยไฟฟ้า : "))

        if units < 0:
            print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ!")
            continue

        cost1, cost2, cost3, cost4, service, total = calculate_electricity_cost(units)

        print("\n--- รายละเอียดค่าไฟ ---")
        print(f"1-50 หน่วยแรก:   {cost1:.2f} บาท")
        print(f"51-100 หน่วย:    {cost2:.2f} บาท")
        print(f"101-200 หน่วย:   {cost3:.2f} บาท")
        print(f"เกิน 200 หน่วย:   {cost4:.2f} บาท")
        print(f"ค่าบริการ:        {service:.2f} บาท")
        print(f"รวมค่าไฟทั้งสิ้น:   {total:.2f} บาท")

    elif choice == "2":
        print("ออกจากโปรแกรมเรียบร้อย")
        break
    else:
        print("ตัวเลือกไม่ถูกต้อง กรุณาเลือก 1 หรือ 2 เท่านั้น")