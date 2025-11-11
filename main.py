from tkinter import *
import sqlite3

conn = sqlite3.connect("reminders.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS reminders (
    title TEXT,
    date TEXT,
    time TEXT
)""")
conn.commit()

root = Tk()
root.title("Smart Student Reminder System")
root.geometry("400x400")

Label(root, text="Smart Student Reminder System", font=("Arial", 16, "bold")).pack(pady=20)

Label(root, text="Reminder Title").pack()
title_entry = Entry(root, width=30)
title_entry.pack()

Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = Entry(root, width=30)
date_entry.pack()

Label(root, text="Time (HH:MM)").pack()
time_entry = Entry(root, width=30)
time_entry.pack()

def add_reminder():
    title = title_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    c.execute("INSERT INTO reminders VALUES (?, ?, ?)", (title, date, time))
    conn.commit()

    Label(root, text="✅ Reminder Saved!", fg="green").pack()

Button(root, text="Add Reminder", command=add_reminder).pack(pady=10)
def view_reminders():
    c.execute("SELECT * FROM reminders")
    rows = c.fetchall()
    for row in rows:
        Label(root, text=f"{row[0]} - {row[1]} {row[2]}").pack()

Button(root, text="View Reminders", command=view_reminders).pack(pady=10)


root.mainloop()
