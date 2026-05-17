import tkinter
import time
from tkinter import messagebox

# Create Window
window = tkinter.Tk()

# Window Title
window.title("GST Calculator")

# Window Size
window.geometry("400x650")

# Background Color
window.config(bg="#1e1e1e")

# Heading
heading = tkinter.Label(
    window,
    text="GST Calculator",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)

heading.pack(pady=15)

# Time Label
time_label = tkinter.Label(
    window,
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="#00ff99"
)

time_label.pack()

# Live Clock Function
def update_time():

    current_time = time.strftime(
        "%d-%m-%Y  %I:%M:%S %p"
    )

    time_label.config(text=current_time)

    window.after(1000, update_time)

# Start Clock
update_time()

# Price Label
price_label = tkinter.Label(
    window,
    text="Enter Price",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

price_label.pack(pady=5)

# Price Entry
price_entry = tkinter.Entry(
    window,
    font=("Arial", 14),
    width=20
)

price_entry.pack(pady=5)

# GST Label
gst_label = tkinter.Label(
    window,
    text="Enter GST %",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

gst_label.pack(pady=5)

# GST Entry
gst_entry = tkinter.Entry(
    window,
    font=("Arial", 14),
    width=20
)

gst_entry.pack(pady=5)

# Result Label
result_label = tkinter.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e",
    fg="#00ff99"
)

result_label.pack(pady=15)

# History Title
history_title = tkinter.Label(
    window,
    text="History",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)

history_title.pack()

# History Box
history_box = tkinter.Text(
    window,
    height=12,
    width=42,
    bg="#2d2d2d",
    fg="white",
    font=("Arial", 10)
)

history_box.pack(pady=10)

# Load Old History
try:

    file = open("history.txt", "r")

    old_history = file.read()

    history_box.insert(tkinter.END, old_history)

    file.close()

except:
    pass

# GST Function
def calculate_gst():

    try:

        # Input
        price = float(price_entry.get())

        gst_percent = float(gst_entry.get())

        # GST Calculation
        gst_amount = (price * gst_percent) / 100

        final_price = price + gst_amount

        # Show Result
        result_label.config(
            text=f"GST = {gst_amount}\nFinal Price = {final_price}"
        )

        # History Text
        history_text = (
            f"{time.strftime('%d-%m-%Y %I:%M:%S %p')} | "
            f"Price: {price} | "
            f"GST: {gst_percent}% | "
            f"Total: {final_price}\n"
        )

        # Add History
        history_box.insert(tkinter.END, history_text)

        # Save History File
        file = open("history.txt", "a")

        file.write(history_text)

        file.close()

        # Export Bill
        bill_file = open("latest_bill.txt", "w")

        bill_file.write(
            "===== GST BILL =====\n\n"
        )

        bill_file.write(
            f"Date & Time: "
            f"{time.strftime('%d-%m-%Y %I:%M:%S %p')}\n"
        )

        bill_file.write(
            f"Price: {price}\n"
        )

        bill_file.write(
            f"GST %: {gst_percent}\n"
        )

        bill_file.write(
            f"GST Amount: {gst_amount}\n"
        )

        bill_file.write(
            f"Final Price: {final_price}\n"
        )

        bill_file.close()

        # Clear Inputs
        price_entry.delete(0, tkinter.END)

        gst_entry.delete(0, tkinter.END)

    except:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )

# Clear History Function
def clear_history():

    history_box.delete("1.0", tkinter.END)

    file = open("history.txt", "w")

    file.close()

# Calculate Button
calculate_button = tkinter.Button(
    window,
    text="Calculate GST",
    font=("Arial", 12, "bold"),
    bg="#00ff99",
    fg="black",
    padx=10,
    pady=5,
    command=calculate_gst
)

calculate_button.pack(pady=10)

# Clear Button
clear_button = tkinter.Button(
    window,
    text="Clear History",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    padx=10,
    pady=5,
    command=clear_history
)

clear_button.pack(pady=5)

# Run App
window.mainloop()