print("โปรแกรมคำนวณเลขสูตรคูณ V.2")
n = int(input("แม่สูตรคูณเริ่มต้น : "))
m = int(input("แม่สูตรคูณสุดท้าย : "))

for b in range(n, m + 1):
    print(f"\nสูตรคูณของ{b}:")
    for i in range(1, 13):
        print(f"{b} x {i} = {b*i}")

print("Coding by kittiphas rachlek No.8 M.4/4")