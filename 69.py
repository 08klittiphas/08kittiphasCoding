print("โปรแกรมคำนวณและแสดงคะแนนสอบรวมรายวิชาวิทยาศาสตร์ By Kitiiphaslnwza007 \n")

Physics = int(input("คะแนนฟิสิกส์ของคุณได้เท่าไหร่"))
Chemistry = int(input("คะแนนเคมีคุณได้เท่าไหร่"))
Biology = int(input("คะแนนชีวะคุณได้เท่าไหร่"))

total =  (Physics + Chemistry + Biology)
average = total/3
print("คะแนนรวม 3 วิชาได้ \nคือ" ,total, "คะแนน")
print("คะแนนเฉลี่ยของ 7 ทั้ง 3 วิชา \nคือ " ,average, "คะแนน")
if average >=80 :
    print("ดีเยี่ยม\n")
elif average >= 60:
    print("ผ่าน\n")
else:
    print("ควรปรับปรุง\n")

print("ชื่นชมและให้กำลังใจสำหรับคนที่ผ่านและไม่ผ่านครับ")
print("ขอบคุณครับ ที่ใช้โปรแกรมคำนวณและแสดงผลคะแนนสอบ\n")
print("Coding by Kittiphaslnwza007")