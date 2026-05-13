# Import the tkinter library
import tkinter as tk


# Create empty lists to store names and scores
names = []
scores = []


# Function to add a student score
def add_score():

    # Get the values from the entry boxes
    name = name_entry.get()
    score = score_entry.get()

    # Check if the score is a whole number
    if score.isdigit() == True:

        # Convert score into an integer
        score = int(score)

        # Validate the score range
        if score >= 0 and score <= 100:

            # Store data in the lists
            names.append(name)
            scores.append(score)

            # Display the student in the listbox
            score_list.insert(
                tk.END,
                name + " - " + str(score)
            )

            # Clear the input boxes
            name_entry.delete(0, tk.END)
            score_entry.delete(0, tk.END)

            # Show how many students have been entered
            output_label.config(
                text="Students entered: " + str(len(names)) + "/8"
            )

        else:

            # Score is outside the valid range
            output_label.config(
                text="Score must be between 0 and 100. Please re-enter the score."
            )

            # Clear only the score box
            score_entry.delete(0, tk.END)

    else:

        # Score is not a number
        output_label.config(
            text="Score must be a whole number. Please re-enter the score."
        )

        # Clear only the score box
        score_entry.delete(0, tk.END)


# Function to calculate awards
def calculate_awards():

    # Check that 8 students have been entered
    if len(names) != 8:

        output_label.config(
            text="Please enter all 8 students."
        )

    else:

        # Create copies of the lists
        sorted_scores = scores.copy()
        sorted_names = names.copy()

        # Bubble sort from highest to lowest
        for pass_number in range(len(sorted_scores) - 1):

            for index in range(len(sorted_scores) - 1):

                if sorted_scores[index] < sorted_scores[index + 1]:

                    # Swap scores
                    temp_score = sorted_scores[index]
                    sorted_scores[index] = sorted_scores[index + 1]
                    sorted_scores[index + 1] = temp_score

                    # Swap names
                    temp_name = sorted_names[index]
                    sorted_names[index] = sorted_names[index + 1]
                    sorted_names[index + 1] = temp_name

        # Create the results message
        result = "🏆 Coding Challenge Awards\n\n"

        result = result + "🥇 Gold Award\n"
        result = result + sorted_names[0]
        result = result + " - " + str(sorted_scores[0]) + "\n\n"

        result = result + "🥈 Silver Award\n"
        result = result + sorted_names[1]
        result = result + " - " + str(sorted_scores[1]) + "\n\n"

        result = result + "🥉 Bronze Award\n"
        result = result + sorted_names[2]
        result = result + " - " + str(sorted_scores[2])

        # Display results
        output_label.config(text=result)


# Create the main window
window = tk.Tk()

# Set window title
window.title("Dragons Coding Awards")

# Set window size
window.geometry("500x600")


# ---------- Title ----------

title_label = tk.Label(
    window,
    text="🐉 Dragons Coding Challenge Awards",
    font=("Arial", 18)
)
title_label.pack(pady=10)


# ---------- Name Input ----------

name_label = tk.Label(window, text="Student Name")
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack()


# ---------- Score Input ----------

score_label = tk.Label(window, text="Challenge Score / 100")
score_label.pack()

score_entry = tk.Entry(window, width=30)
score_entry.pack(pady=10)


# ---------- Add Button ----------

add_button = tk.Button(
    window,
    text="Add Score",
    command=add_score
)
add_button.pack(pady=10)


# ---------- Listbox ----------

score_list = tk.Listbox(window, width=40, height=10)
score_list.pack(pady=10)


# ---------- Award Button ----------

award_button = tk.Button(
    window,
    text="Calculate Awards",
    command=calculate_awards
)
award_button.pack(pady=10)


# ---------- Output ----------

output_label = tk.Label(
    window,
    text="",
    justify="left",
    wraplength=400
)
output_label.pack(pady=20)


# Keep the window running
window.mainloop()
