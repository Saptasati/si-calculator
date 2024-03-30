import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        result = round((p * r * t) / 100, 2)
        result_label.config(text=f"Simple Interest: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for Principal, Rate, and Time.")

def destroy_label():
    heading_label.destroy()

# Create parent window
root = tk.Tk()
root.geometry("400x300")
root.title("Simple Interest Calculator")
root.configure(bg='lightgrey')

# Heading Label
heading_label = tk.Label(root, text="Simple Interest Calculator", font=("Helvetica", 16), bg='lightgrey')
heading_label.place(x=100, y=20)

# Principal Label and Entry
label_principal = tk.Label(root, text="Principal:", bg='lightgrey')
label_principal.place(x=50, y=60)
entry_principal = tk.Entry(root)
entry_principal.place(x=150, y=60)

# Rate of Interest Label and Entry
label_rate = tk.Label(root, text="Rate of Interest:", bg='lightgrey')
label_rate.place(x=50, y=90)
entry_rate = tk.Entry(root)
entry_rate.place(x=150, y=90)

# Time Label and Entry
label_time = tk.Label(root, text="Time:", bg='lightgrey')
label_time.place(x=50, y=120)
entry_time = tk.Entry(root)
entry_time.place(x=150, y=120)

# Calculation Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.place(x=180, y=150)

# Result Frame Container
result_frame = tk.LabelFrame(root, text="Result", bg='lightgrey')
result_frame.place(x=50, y=200, width=300, height=80)

# Result Label
result_label = tk.Label(result_frame, text="", bg='lightgrey')
result_label.pack()

root.mainloop()
