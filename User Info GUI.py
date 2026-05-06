import tkinter as tk

def submit_details():
    name = name_entry.get()
    age = age_entry.get()
    tutor = tutor_entry.get()

    message = "Student Details\n"
    message = message + "Name: " + name + "\n"
    message = message + "Age: " + age + "\n"
    message = message + "Tutor Group: " + tutor

    output_label.config(text=message)

window = tk.Tk()
window.title("Student Information Form")
window.geometry("400x300")

title_label = tk.Label(window, text="Enter Your Details", font=("Arial", 16))
title_label.pack(pady=10)

name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()

age_entry = tk.Entry(window, width=30)
age_entry.pack()

tutor_label = tk.Label(window, text="Tutor Group:")
tutor_label.pack()

tutor_entry = tk.Entry(window, width=30)
tutor_entry.pack()

submit_button = tk.Button(window, text="Submit", command=submit_details)
submit_button.pack(pady=15)

output_label = tk.Label(window, text="", justify="left")
output_label.pack(pady=10)

window.mainloop()
