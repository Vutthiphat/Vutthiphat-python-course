scores = []
for i in range(5):
    s = float(input(f"กรอกคะแนนนักเรียนคนที่ {i+1}: "))
    scores.append(s)

print("\n--- ผลการสอบ ---")
for i in range(len(scores)):
    if scores[i] >= 50:
        print(f"นักเรียนคนที่ {i+1} คะแนน {scores[i]} : ผ่าน")
    else:
        print(f"นักเรียนคนที่ {i+1} คะแนน {scores[i]} : ไม่ผ่าน")