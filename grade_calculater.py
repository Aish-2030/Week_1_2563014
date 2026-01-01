from tkinter import *

def calculate():
  
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

    

root = Tk()
root.title("Student Grade Calculator")
root.geometry("320x300")

title = Label(root, text="Grade Calculator", font=("Arial", 16, "bold") ,bg="lightblue")
title.pack(pady=10)


Label(root, text="Subject 1 Marks:",bg="lightgreen").pack()
sub1_entry = Entry(root)
sub1_entry.pack()

Label(root, text="Subject 2 Marks:",bg="lightgreen").pack()
sub2_entry = Entry(root)
sub2_entry.pack()

Label(root, text="Subject 3 Marks:",bg="lightgreen").pack()
sub3_entry = Entry(root)
sub3_entry.pack()


btn = Button(root, text="Calculate", command=calculate,bg="orange")
btn.pack(pady=10)


total_label = Label(root, text="", font=("Arial", 12),bg="lightpink")
total_label.pack()

avg_label = Label(root, text="", font=("Arial", 12),bg="lightpink")
avg_label.pack()

grade_label = Label(root, text="", font=("Arial", 12),bg="lightpink")
grade_label.pack()

root.mainloop()

