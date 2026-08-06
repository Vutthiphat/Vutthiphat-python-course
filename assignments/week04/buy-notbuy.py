prices = []
for i in range(6):
    p = float(input(f"กรอกราคาสินค้าชิ้นที่ {i+1}: "))
    prices.append(p)

budget = float(input("กรอกงบประมาณรวม: "))

bought_items = []
total_spent = 0

print("\n--- ผลการตัดสินใจซื้อสินค้า ---")
for i in range(len(prices)):
    item_price = prices[i]
    if total_spent + item_price <= budget:
        print(f"สินค้าชิ้นที่ {i+1} ราคา {item_price} : buy")
        total_spent = total_spent + item_price
        bought_items.append(item_price)
    else:
        print(f"สินค้าชิ้นที่ {i+1} ราคา {item_price} : cannot buy")

remaining_budget = budget - total_spent

print(f"\nรายการสินค้าที่ซื้อได้: {bought_items}")
print(f"ยอดใช้จ่ายรวม: {total_spent}")
print(f"งบประมาณคงเหลือ: {remaining_budget}")