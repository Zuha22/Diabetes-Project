import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class DiabetesDiagnosisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Diabetes Diagnosis")
        #background image
        background_image = Image.open("C:/medical.jpg")

        # Resize the image to fit the screen
        background_image = background_image.resize((self.master.winfo_screenwidth(), self.master.winfo_screenheight()))

        # Convert the image to Tkinter format
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Set the theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Configure a custom style with padding
        self.style.configure("Question.TLabel", font=('Arial', 14), padding=(20, 20))

        # Create a label with the background image
        self.background_label = tk.Label(self.master, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Send the background label to the back
        self.background_label.lower()

        # Initialize questions and responses
        self.symptoms = {
            "polyuria": tk.BooleanVar(),
            "polydipsia": tk.BooleanVar(),
            "weight_loss": tk.BooleanVar(),
            "ketoacidosis": tk.BooleanVar(),
            "weakness": tk.BooleanVar(),
            "increased_appetite": tk.BooleanVar(),
            "blurred_vision": tk.BooleanVar(),
            "persistent_itching": tk.BooleanVar(),
            "slow_healing": tk.BooleanVar(),
            "hypertension": tk.BooleanVar(),
            "obesity": tk.BooleanVar(),
            "family_history": tk.BooleanVar(),
        }

        self.questions = [
            "Have you noticed increased urination and the need to urinate frequently?",
            "Have you noticed increased thirst and a desire to drink excessive amounts of fluid?",
            "Have you noticed significant weight loss that you cannot explain?",
            "Have you experienced an unexplained ketosis (ketchup-smelling breath, vomiting, confusion, etc.)?",
            "Have you noticed unexplained fatigue or weakness?",
            "Have you noticed an increased hunger or craving for sweet, starchy, or fatty foods?",
            "Have you noticed blurred vision, increased light sensitivity, or reduced visual acuity?",
            "Have you experienced persistent itching or discomfort that is not related to a known skin condition?",
            "Have you noticed slow healing wounds or reduced resistance to infections?",
            "Do you have a family history of diabetes?",
            "Are you aware of any health conditions that could affect blood sugar levels?",
        ]

        self.current_question_index = 0

        # Display the first question
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            self.question_label = ttk.Label(
                self.master,
                text=self.questions[self.current_question_index],
                style="Question.TLabel"  # Apply the custom style
            )
            self.question_label.grid(row=0, column=0, columnspan=2, pady=40, padx=20, sticky=tk.W + tk.E + tk.N + tk.S)  # Center the label

            self.yes_button = ttk.Button(self.master, text="Yes", command=lambda: self.record_response(True), style="TButton")
            self.yes_button.grid(row=1, column=0, pady=20, padx=20, sticky=tk.W)

            self.no_button = ttk.Button(self.master, text="No", command=lambda: self.record_response(False), style="TButton")
            self.no_button.grid(row=1, column=1, pady=20, padx=20, sticky=tk.W)
        else:
            self.diabetes_diagnosis()

    def record_response(self, response):
        symptom = list(self.symptoms.keys())[self.current_question_index]
        self.symptoms[symptom].set(response)
        self.current_question_index += 1
        self.show_question()

    def diabetes_diagnosis(self):
        # Rule-based conditions for diabetes type diagnosis
        if (
                self.symptoms['polyuria'].get()
                and self.symptoms['polydipsia'].get()
                and self.symptoms['weight_loss'].get()
        ):
            if self.symptoms['weakness'].get() and self.symptoms['increased_appetite'].get():
                result = "Type 1 Diabetes"
            else:
                result = "Type 2 Diabetes"
        elif (
                self.symptoms['blurred_vision'].get()
                and self.symptoms['persistent_itching'].get()
                and self.symptoms['slow_healing'].get()
        ):
            result = "Likely to be Diabetes related to insulin resistance"
        elif (
                self.symptoms['polyuria'].get()
                and self.symptoms['polydipsia'].get()
                and self.symptoms['weight_loss'].get()
                and self.symptoms['ketoacidosis'].get()
        ):
            result = "Likely to be Type 1 Diabetes with Ketoacidosis"
        else:
            result = "Unable to diagnose based on provided symptoms"

        # Display result
        result_label = ttk.Label(self.master, text=result, font=('Arial', 20, 'bold'))
        result_label.grid(row=2, column=0, columnspan=2, pady=20)

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = DiabetesDiagnosisApp(root)
    root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))
    root.mainloop()

if __name__ == '__main__':
    main()
