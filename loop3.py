print("โปรแกรมทายจำนวน By 08")
import random
number  = random.randint(1,100)
count = 1
while True:
    guess = int(input("ทายเลข: "))
    count += 1

    if guess > number:
        print("มากไป")
    elif guess < number:
        print("น้อยไป")
    else:
        print(f"ถูกต้อง ทายไปทั้งหมด {count}ครั้ง")