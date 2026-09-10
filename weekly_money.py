def get_money(message):
    """รับจำนวนเงินและตรวจสอบข้อมูล"""
    while True:
        try:
            amount = float(input(message))

            if amount < 0:
                print("กรุณากรอกจำนวนเงินที่ไม่ติดลบ")
                continue

            return amount

        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")


def get_percentage(message):
    """รับเปอร์เซ็นต์และตรวจสอบข้อมูล"""
    while True:
        try:
            percent = float(input(message))

            if percent < 0 or percent > 100:
                print("เปอร์เซ็นต์ต้องอยู่ระหว่าง 0 - 100")
                continue

            return percent

        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")


def calculate_allocation(income, percentages):
    """คำนวณจำนวนเงินตามเปอร์เซ็นต์"""

    allocation = {}

    for category, percent in percentages.items():
        allocation[category] = income * percent / 100

    return allocation


def display_summary(income, allocation):
    """แสดงผลสรุปการจัดสรรเงิน"""

    print("\n" + "=" * 55)
    print("             สรุปการจัดสรรเงินรายอาทิตย์")
    print("=" * 55)

    print(f"รายได้ทั้งหมด       : {income:,.2f} บาท")
    print("-" * 55)

    total = 0

    for category, amount in allocation.items():
        print(f"{category:<20}: {amount:>10,.2f} บาท")
        total += amount

    print("-" * 55)
    print(f"{'จัดสรรทั้งหมด':<20}: {total:>10,.2f} บาท")

    remaining = income - total

    print(f"{'เงินคงเหลือ':<20}: {remaining:>10,.2f} บาท")

    if remaining > 0:
        print("\nสถานะ: มีเงินเหลือจากการจัดสรร")
    elif remaining == 0:
        print("\nสถานะ: จัดสรรเงินครบพอดี")
    else:
        print("\nสถานะ: จัดสรรเงินเกินรายได้!")

    print("=" * 55)


def save_summary(income, allocation):
    """บันทึกสรุปลงไฟล์"""

    total = sum(allocation.values())
    remaining = income - total

    try:
        with open("weekly_money_summary.txt", "w", encoding="utf-8") as file:

            file.write("====================================\n")
            file.write("       สรุปการจัดสรรเงินรายอาทิตย์\n")
            file.write("====================================\n\n")

            file.write(f"รายได้ทั้งหมด: {income:,.2f} บาท\n\n")

            for category, amount in allocation.items():
                file.write(
                    f"{category}: {amount:,.2f} บาท\n"
                )

            file.write("\n")
            file.write(
                f"จัดสรรทั้งหมด: {total:,.2f} บาท\n"
            )

            file.write(
                f"เงินคงเหลือ: {remaining:,.2f} บาท\n"
            )

        print("\nบันทึกข้อมูลเรียบร้อยแล้ว")
        print("ไฟล์: weekly_money_summary.txt")

    except OSError:
        print("ไม่สามารถบันทึกไฟล์ได้")


def main():
    """ฟังก์ชันหลักของโปรแกรม"""

    print("=" * 55)
    print("       โปรแกรมจัดสรรเงินรายอาทิตย์")
    print("=" * 55)

    # รับรายได้
    income = get_money(
        "\nกรอกรายได้ต่ออาทิตย์ (บาท): "
    )

    print("\nกำหนดเปอร์เซ็นต์การจัดสรรเงิน")
    print("เปอร์เซ็นต์รวมควรไม่เกิน 100%")

    # รับเปอร์เซ็นต์
    percentages = {}

    percentages["ค่าอาหาร"] = get_percentage(
        "ค่าอาหาร (%): "
    )

    percentages["ค่าเดินทาง"] = get_percentage(
        "ค่าเดินทาง (%): "
    )

    percentages["ค่าใช้จ่ายจำเป็น"] = get_percentage(
        "ค่าใช้จ่ายจำเป็น (%): "
    )

    percentages["เงินออม"] = get_percentage(
        "เงินออม (%): "
    )

    percentages["เงินฉุกเฉิน"] = get_percentage(
        "เงินฉุกเฉิน (%): "
    )

    percentages["เงินใช้ส่วนตัว"] = get_percentage(
        "เงินใช้ส่วนตัว (%): "
    )

    # ตรวจสอบเปอร์เซ็นต์รวม
    total_percentage = sum(percentages.values())

    print(
        f"\nเปอร์เซ็นต์รวม: {total_percentage:.2f}%"
    )

    if total_percentage > 100:
        print("\nไม่สามารถจัดสรรได้")
        print("เปอร์เซ็นต์รวมมากกว่า 100%")
        return

    # คำนวณ
    allocation = calculate_allocation(
        income,
        percentages
    )

    # แสดงผล
    display_summary(
        income,
        allocation
    )

    # ถามการบันทึก
    save = input(
        "\nต้องการบันทึกข้อมูลหรือไม่? (y/n): "
    ).strip().lower()

    if save == "y":
        save_summary(
            income,
            allocation
        )

    print("\nจบการทำงานของโปรแกรม")
    print("ขอบคุณที่ใช้โปรแกรม")


# ==========================================
# เริ่มต้นโปรแกรม
# ==========================================

if __name__ == "__main__":
    main()