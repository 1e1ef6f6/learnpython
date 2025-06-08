# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)
import math


side = int(input("จำนวนด้าน: "))
long_side = int(input("ความยาวด้าน: "))
cal = (side * pow(long_side, 2)) / (4 * math.tan(math.pi / side))

print(f"รูปหลายเหลี่ยมที่มี {side} ด้าน และความยาวด้านละ {long_side} หน่วย จะมีพื้นที่เท่ากับ {cal:.3f}")