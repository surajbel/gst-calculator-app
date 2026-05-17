history = []

while True:

    print("\n=== GST Calculator ===")

    price = float(input("Enter price: "))
    gst_percent = float(input("Enter GST %: "))

    gst_amount = (price * gst_percent) / 100
    final_price = price + gst_amount

    print("GST Amount:", gst_amount)
    print("Final Price:", final_price)

    # Save history
    bill = f"{price} | {gst_percent}% | GST={gst_amount} | Total={final_price}"

    history.append(bill)

    print("\n=== History ===")

    for item in history:
        print(item)

    again = input("\nDo another calculation? (yes/no): ")

    if again == "no":
        break