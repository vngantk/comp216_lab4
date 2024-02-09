from tkinter import *
from tkinter import ttk
from tkinter import messagebox

RESIDENCY_DICT = {
    "dom": "Domestic",
    "intl": "International"
}

PROGRAM_LIST = ["AI", "Gaming", "Health", "Software"]

COURSE_DICT = {
    "COMP100": "Programming I",
    "COMP213": "Web Page Design",
    "COMP120": "Software Engineering"
}


class StudentSurveyForm(Frame):

    def __init__(self, master: Tk = Tk()):
        super().__init__(master)
        master.title("Centennial College")
        self.pack(fill=Y, expand=True, padx=10, pady=5)
        self.columnconfigure(0, minsize=120)
        self.columnconfigure(1, minsize=150)
        self.columnconfigure(2, minsize=150)
        self.rowconfigure(8, weight=1)
        row = 0

        Label(self, text="ICET Student Survey", font=("Arial", 20, "bold italic")).grid(row=row, column=0, columnspan=3, pady=10)
        row += 1

        # Full name
        Label(self, text="Full name:").grid(row=row, column=0, sticky="w", padx=0, pady=2)
        self.username_entry = Entry(self, width=20)
        self.username_entry.grid(row=row, column=1, columnspan=2, padx=0, pady=2, sticky="w")
        row += 1

        # Residency
        Label(self, text="Residency:").grid(row=row, column=0, sticky="w", padx=0, pady=2)
        self.residency_var = StringVar()
        for i, (code, text) in enumerate(RESIDENCY_DICT.items()):
            Radiobutton(self, text=text, variable=self.residency_var, value=code).grid(row=row, column=1, columnspan=2, sticky="w", padx=0, pady=2)
            row += 1

        # Program
        Label(self, text="Program:").grid(row=row, column=0, sticky="w", padx=0, pady=2)
        self.program_combobox = ttk.Combobox(self, width=10, values=PROGRAM_LIST)
        self.program_combobox.grid(row=row, column=1, columnspan=1, padx=0, pady=2, sticky="w")
        row += 1

        # Courses
        Label(self, text="Courses:").grid(row=row, column=0, sticky="nw", padx=0, pady=2)
        self.course_checked = {}
        for i, (code, name) in enumerate(COURSE_DICT.items()):
            checked = BooleanVar(value=False)
            Checkbutton(self, text=name, onvalue=True, offvalue=False, variable=checked).grid(row=row, column=1, sticky="w", padx=0, pady=2)
            self.course_checked[code] = checked
            row += 1

        # Buttons
        Button(self, text="Reset", command=self.reset).grid(row=row, column=0, pady=5, sticky="sew")
        Button(self, text="Ok", command=self.ok).grid(row=row, column=1, pady=5, sticky="sew")
        Button(self, text="Exit", command=self.quit).grid(row=row, column=2, pady=5, sticky="sew")
        row += 1
        self.reset()

    def reset(self):
        self.username_entry.delete(0, END)
        self.username_entry.insert(0, "Tsang Kwong Ngan")
        self.residency_var.set("intl")
        self.program_combobox.set("AI")
        for code in COURSE_DICT.keys():
            self.course_checked[code].set(False)

    def ok(self):
        username = self.username_entry.get()
        residency = self.residency_var.get()
        program = self.program_combobox.get()
        courses = []
        for code, checked in self.course_checked.items():
            if checked.get():
                courses.append(code)
        messagebox.showinfo(
            title="Information",
            message=username + "\n" + program + "\n" + residency + "\n" + "(" + ",".join(courses) + ")")


StudentSurveyForm().mainloop()
