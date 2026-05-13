# Import the tkinter library so we can create a GUI
import tkinter as tk


# This function runs when the button is clicked
def add_student():

    # Create an empty list to store selected languages
    languages = []

    # Check if each programming language has been ticked
    if python_var.get() == 1:
        languages.append("Python")

    if swift_var.get() == 1:
        languages.append("Swift")

    if cpp_var.get() == 1:
        languages.append("C++")

    if java_var.get() == 1:
        languages.append("Java")

    # Join all selected languages together into one string
    coding_languages = ", ".join(languages)

    # Create a single student record
    student = (
        first_name_entry.get() + " " +
        family_name_entry.get() +
        " | Year " + year_group_entry.get() +
        " | " + coding_years_entry.get() + " years coding" +
        " | Languages: " + coding_languages
    )

    # Add the student record to the listbox
    student_list.insert(tk.END, student)

    # Clear all input boxes after adding a student
    first_name_entry.delete(0, tk.END)
    family_name_entry.delete(0, tk.END)
    year_group_entry.delete(0, tk.END)
    coding_years_entry.delete(0, tk.END)

    # Untick all checkboxes
    python_var.set(0)
    swift_var.set(0)
    cpp_var.set(0)
    java_var.set(0)


# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Dragons Coding Registration")

# Set the size of the window
window.geometry("600x500")


# Create the title label
title_label = tk.Label(
    window,
    text="Dragons Coding Registration",
    font=("Arial", 18)
)
title_label.pack(pady=10)


# ---------- First Name ----------

first_name_label = tk.Label(window, text="First Name")
first_name_label.pack()

# Entry box for first name
first_name_entry = tk.Entry(window, width=30)
first_name_entry.pack()


# ---------- Family Name ----------

family_name_label = tk.Label(window, text="Family Name")
family_name_label.pack()

family_name_entry = tk.Entry(window, width=30)
family_name_entry.pack()


# ---------- Year Group ----------

year_group_label = tk.Label(window, text="Year Group")
year_group_label.pack()

year_group_entry = tk.Entry(window, width=30)
year_group_entry.pack()


# ---------- Years Coding ----------

coding_years_label = tk.Label(window, text="Years Coding")
coding_years_label.pack()

coding_years_entry = tk.Entry(window, width=30)
coding_years_entry.pack(pady=10)


# ---------- Programming Languages ----------

languages_label = tk.Label(window, text="Programming Languages")
languages_label.pack()

# Variables used to store checkbox values
python_var = tk.IntVar()
swift_var = tk.IntVar()
cpp_var = tk.IntVar()
java_var = tk.IntVar()

# Create checkboxes
python_check = tk.Checkbutton(
    window,
    text="Python",
    variable=python_var
)
python_check.pack()

swift_check = tk.Checkbutton(
    window,
    text="Swift",
    variable=swift_var
)
swift_check.pack()

cpp_check = tk.Checkbutton(
    window,
    text="C++",
    variable=cpp_var
)
cpp_check.pack()

java_check = tk.Checkbutton(
    window,
    text="Java",
    variable=java_var
)
java_check.pack()


# ---------- Add Student Button ----------

# When clicked, this button runs the add_student function
add_button = tk.Button(
    window,
    text="Add Student",
    command=add_student
)
add_button.pack(pady=15)


# ---------- Output List ----------

# Listbox used to display all students entered
student_list = tk.Listbox(window, width=80, height=10)
student_list.pack(pady=10)


# Keep the window running
window.mainloop()
