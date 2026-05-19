import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys

# Finding Path
thisFolder = os.path.dirname(sys.executable)

# Variable
ssc = os.listdir(os.path.join(thisFolder, "Asaiyf Shortcuts")) # ssc means "selected shortcuts"

disclamerPath = os.path.join(thisFolder, "disclamerBox.cfg")

# Function
def runFile():
    try:
        selected_item = dropdown.get()
        if selected_item:
            file = os.path.join(thisFolder, "Asaiyf Shortcuts", selected_item)
            os.startfile(file)
    except FileNotFoundError:
        messagebox.showerror("Failure", 'Error: File Not Found, Click "Update List" And Select A Different One')
    except Exception as e:
        messagebox.showerror("Error", f"An Error Has Occurred: {e}")

def updateList():
    global ssc
    ssc = os.listdir(os.path.join(thisFolder, "Asaiyf Shortcuts"))
    dropdown["values"] = ssc

def disclamerOff():
    with open(disclamerPath, "r") as file:
        currentSettings = file.readlines()
    newSettings = []
    for line in currentSettings:
        if line.startswith("showDisclamerOnStartup ="):
            newSettings.append("showDisclamerOnStartup = False")
        else:
            newSettings.append(line)
    with open(disclamerPath, "w") as file:
        file.writelines(newSettings)

with open(disclamerPath, "r") as file:
    currentSettings = file.readlines()
newSettings = []
for line in currentSettings:
    if line.startswith("showDisclamerOnStartup = T"):
        response = messagebox.askyesno("DISCLAMER", "MAKE SURE YOU READ THE README IF YOU HAVEN'T\n\nMake this disclamer never appear again?")
        if response == True:
            disclamerOff()

# Window
window = tk.Tk()
window.title("Asaiyf Minimalist Launcher")
window.geometry("200x200")
window.configure(bg="#b1b1b1")

dropdown = ttk.Combobox(window, values=ssc, state="readonly")
dropdown.pack(pady=20)

button = tk.Button(window, text="Run", font=("Arial", 12), command=runFile)
button.pack(pady=5)

button = tk.Button(window, text="Update List", font=("Arial", 12), command=updateList)
button.pack(pady=5)


# Loop
window.mainloop()
