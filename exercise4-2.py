# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)

weight = input("น้ำหนัก (กิโลกรัม): ")
height = input("ส่วนสูง (cm): ")
height_m = float(height) / 100
bmi = float(weight) / (height_m ** 2)

if bmi >= 40:
    print(f"คุณมีภาวะอ้วนระดับ 3 (อ้วนมาก): {bmi:.2f}")
elif bmi >= 35:
    print(f"คุณมีภาวะอ้วนระดับ 2 (อ้วนกลาง): {bmi:.2f}")
elif bmi >= 28.5:
    print(f"คุณมีภาวะอ้วนระดับ 1 (อ้วนเบา): {bmi:.2f}")
elif bmi >= 23.5:
    print(f"คุณมีภาวะน้ำหนักเกิน (อ้วนท้วม): {bmi:.2f}")
elif bmi >= 18.5:
    print(f"คุณมีภาวะน้ำหนักปกติ: {bmi:.2f}")
else:
    print(f"คุณมีภาวะน้ำหนักต่ำ (ผอม): {bmi:.2f}")