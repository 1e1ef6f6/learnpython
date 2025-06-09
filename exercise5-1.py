# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)



en_num = int(input("EnterNum: "))
remain = en_num
digit = 0
sum = 0

max_digit = 0

while remain != 0:
    digit = remain % 10

    if digit > max_digit:
        max_digit = digit
    

    if digit > 0:
        sum += digit


    # if result == "":
    #     result = str(digit)
    # else:
    #     result = str(digit) + ", " + result
    remain = remain // 10

print(max_digit)
print(sum)

            
