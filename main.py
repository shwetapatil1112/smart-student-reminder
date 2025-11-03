from tkinter import *

root = Tk()
root.title("Smart Student Reminder System")
root.geometry("400x400")

# App heading
Label(root, text="Smart Student Reminder System", font=("Arial", 16, "bold")).pack(pady=20)

# -----------------------------
# Day 2: Add input fields
# -----------------------------
Label(root, text="Reminder Title").pack()
title_entry = Entry(root, width=30)
title_entry.pack()

Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = Entry(root, width=30)
date_entry.pack()

Label(root, text="Time (HH:MM)").pack()
time_entry = Entry(root, width=30)
time_entry.pack()

Button(root, text="Add Reminder").pack(pady=10)

# -----------------------------
root.mainloop()
