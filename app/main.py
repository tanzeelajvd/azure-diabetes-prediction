import os
import webbrowser
from tkinter import *

# ---------- Paths ----------
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")

# ---------- Callbacks ----------
def run_prediction():
    window.destroy()
    exec(open(os.path.join(SCRIPT_DIR, "azure_diabetic.py")).read())

def open_info():
    webbrowser.open(
        "https://www.webmd.com/diabetes/tc/criteria-for-diagnosing-diabetes-topic-overview"
    )

# ---------- Window ----------
window = Tk()
window.title("Diabetes Diagnostic System")
window.geometry("1000x720")
window.resizable(False, False)
window.configure(bg="#ffffff")

# ---------- Header ----------
header = Frame(window, bg="#1f4e79", height=80)
header.pack(fill=X)

Label(
    header,
    text="Diabetes Diagnostic System",
    bg="#1f4e79",
    fg="white",
    font=("Helvetica", 18, "bold")
).pack(pady=(18, 2))

Label(
    header,
    text="Azure Machine Learning Based Prediction",
    bg="#1f4e79",
    fg="#dce6f1",
    font=("Helvetica", 10)
).pack()

# ---------- Content ----------
content = Frame(window, bg="#ffffff")
content.pack(expand=True)

predict_img = PhotoImage(file=os.path.join(ASSETS_DIR, "givee.gif"))
info_img = PhotoImage(file=os.path.join(ASSETS_DIR, "visitt.gif"))

# Use grid for structure
predict_btn = Button(
    content,
    image=predict_img,
    text="Predict Diabetes",
    compound=TOP,
    font=("Helvetica", 11, "bold"),
    command=run_prediction,
    bd=1,
    relief=SOLID,
    padx=10,
    pady=8
)
predict_btn.grid(row=0, column=0, padx=40, pady=(40, 20))

info_btn = Button(
    content,
    image=info_img,
    text="Learn About Diabetes",
    compound=TOP,
    font=("Helvetica", 10),
    command=open_info,
    bd=1,
    relief=SOLID,
    padx=10,
    pady=8
)
info_btn.grid(row=1, column=0, padx=40)

# ---------- Footer ----------
footer = Label(
    window,
    text="Academic Prototype • Microsoft Azure ML",
    bg="#ffffff",
    fg="#6b7280",
    font=("Helvetica", 9)
)
footer.pack(pady=8)

window.mainloop()
