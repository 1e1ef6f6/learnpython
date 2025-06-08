# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)
import math

amount = int(input("จำนวนเงินทุนเริ่ม: "))
rate = float(input("อัตราดอกเบี้ยต่อปี(%): "))
period = float(input("ระยะเวลาที่ฝาก (ปี): "))
fv = format(amount * math.pow(1 + rate, period), ",.2f")

print(f"มูลค่าเงินลงทุนในอนาคต: {fv} บาท")