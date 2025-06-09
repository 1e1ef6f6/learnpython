# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)

year = input("ปี พ.ศ.: ")
cal = int(year) - 543

if (cal % 100 != 0) and (cal % 4 == 0):
    print(f"{year} เป็นปีอธิกสุรทิน")
else:
    print(f"{year} ไม่เป็นปีอธิกสุรทิน")
