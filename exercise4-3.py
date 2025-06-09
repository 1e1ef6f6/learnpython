# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)

salary = input("เงินเดือน: ")
income_y = float(salary) * 12
income_tax = income_y 




if income_tax <= 150000:
    print(f"คุณไม่ต้องเสียภาษี: {income_tax} บาท")
elif income_tax >= 150001 and income_tax <= 300000:
    tax = format(income_tax * 0.05, ',.2f')
    print(f"คุณต้องเสียภาษี 5%: {tax} บาท")
elif income_tax >= 300001 and income_tax <= 500000:
    tax = format(income_tax * 0.1, ',.2f')
    print(f"คุณต้องเสียภาษี 10%: {tax} บาท")
elif income_tax >= 500001 and income_tax <= 750000:
    tax = format(income_tax * 0.15, ',.2f')
    print(f"คุณต้องเสียภาษี 15%: {tax} บาท")
elif income_tax >= 750001 and income_tax <= 1000000:
    tax = format(income_tax * 0.2, ',.2f')
    print(f"คุณต้องเสียภาษี 20%: {tax} บาท")
elif income_tax >= 1000001 and income_tax <= 2000000:
    tax = format(income_tax * 0.25, ',.2f')
    print(f"คุณต้องเสียภาษี 25%: {tax} บาท")
elif income_tax >= 2000001 and income_tax <= 4000000:
    tax = format(income_tax * 0.3, ',.2f')
    print(f"คุณต้องเสียภาษี 30%: {tax} บาท")
elif income_tax > 4000001:
    tax = format(income_tax * 0.35, ',.2f')
    print(f"คุณต้องเสียภาษี 35%: {tax} บาท")