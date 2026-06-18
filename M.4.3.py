score_english = int(input("คะแนนอังกฤษของคุณได้เท่าไหร่"))
score_math = int(input("คะแนนคณิตคุณได้เท่าไหร่"))
score_science = int(input("คะแนนวิทยาศาสตร์คุณได้เท่าไหร่"))
total_score =  (score_english + score_math + score_science)
average = total_score/3
print("คะแนนรวม 3 วิชาได้" ,total_score, "คะแนน")
print("คะแนนเฉลี่ยของ 7 ทั้ง 3 วิชาคือ " ,average, "คะแนน")
if average >=80 :
    print("ดีเยี่ยม")
elif average >= 60:
    print("ผ่าน")
else:
    print("ควรปรับปรุง")