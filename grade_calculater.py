from tkinter import *

def calculate():
    try:
        m1 = float(sub1_entry.get())
        m2 = float(sub2_entry.get())
        m3 = float(sub3_entry.get())

        total = m1 + m2 + m3
        avg = total / 3

        # grade logic
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "Fail"

        total_label.config(text=f"Total Marks : {total}")
        avg_label.config(text=f"Average Marks : {avg:.2f}")
        grade_label.config(text=f"Grade : {grade}")

    except ValueError:
        total_label.config(text="Please enter valid marks")
        avg_label.config(text="")
        grade_label.config(text="")

root = Tk()
root.title("Student Grade Calculator")
root.geometry("320x300")

title = Label(root, text="Grade Calculator", font=("Arial", 16, "bold") ,bg="lightblue")
title.pack(pady=10)

# Input fields
Label(root, text="Subject 1 Marks:").pack()
sub1_entry = Entry(root)
sub1_entry.pack()

Label(root, text="Subject 2 Marks:").pack()
sub2_entry = Entry(root)
sub2_entry.pack()

Label(root, text="Subject 3 Marks:").pack()
sub3_entry = Entry(root)
sub3_entry.pack()

# Calculate button
btn = Button(root, text="Calculate", command=calculate)
btn.pack(pady=10)

# Result labels
total_label = Label(root, text="", font=("Arial", 12))
total_label.pack()

avg_label = Label(root, text="", font=("Arial", 12))
avg_label.pack()

grade_label = Label(root, text="", font=("Arial", 12))
grade_label.pack()

root.mainloop()
