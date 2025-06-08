# หนังสือ พื้นฐานการเขียนภาษาPython (บัญชา ปะสีละเตสัง)

import random

a = ("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# b = ("abcdefghijklmnopqrstuvwxyz")

# c = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

password = random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a)

print(f"Your password is: {password}")