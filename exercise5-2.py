# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)


max_people = 6
max_weight = 450

people = 1
total_w = 0

for i in range(max_people):

    w = float(input(f"คนที่ {people} นน.: "))

    if w + total_w >= max_weight:
        print("Over")
        continue
    else:
        people += 1
        total_w += w
print(f"ans: {total_w}")
    
