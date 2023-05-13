# placeholder gui testing
import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog as sd
from shutil import copyfile
import subprocess
from tkinter import ttk
import threading


class test:
    def __init__(self):
        self.var = "hello world"
        self.task = threading.Thread(target=self.run)

    def run(self):
        print(self.var)

    def start(self):
        self.task.start()


class medGui:
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("400x450")
        self._root.resizable(False, False)
        self._root.configure(background="#141316")

        self._topFrame = ttk.Frame(self._root, padding="20 20 22 22", width=350, height=400)
        self._topFrame.pack()
        self._topFrame.pack_propagate(False)
        self._topFrame.place(relx=.5, rely=.5, anchor="center")

        self._icon = tk.PhotoImage(file="assets/githubicon.png")
        self.test = test()

    def addStyle(self):
        teststyle = ttk.Style()

        teststyle.configure("TFrame", background="#1b1c1f")
        teststyle.configure("TButton", font=("Lato", 18), borderwidth=0, background="#1b1c1f",
                            foreground="#c9c2bd", activeforeground="#ffffff",
                            activebackground="#1b1c1f")
        teststyle.configure("TSeparator", background="#ffffff")
        teststyle.configure("header.TLabel", font=("Lato", 24), background="#1b1c1f",
                            foreground="#c9c2bd")
        teststyle.configure("normal.TLabel", font=("Lato", 10), background="#1b1c1f",
                            foreground="#c9c2bd")
        teststyle.configure("TEntry", borderwidth=0, fieldbackground="#1b1c1f", foreground="#c9c2bd",
                            relief="flat", justify="center")

    def addProfile(self):
        filename = filedialog.askopenfilename()
        # did you know that i have spent 3 hours on this thing because of some bug i cant find
        # apparently the fix was removing the window title
        # huh.
        name = sd.askstring("Input Name", "Enter Patient's name")
        if name is None:
            print("no name entered")
            return

        # format name
        name = name.lower()
        name = name.replace(" ", "")
        name = "profiles/" + name + ".pdf"

        copyfile(filename, name)

    def textCommand(self):
        command = sd.askstring("Input Command", "Enter command")
        if command is None:
            return
        else:
            print(command)

    def openCredits(self):
        # TODO improvements
        subprocess.run("chromium https://github.com/JairusBGit/MedAssistant", shell=True)

    def makeWidgets(self):
        ttk.Label(self._topFrame, text="MedAssistant", style="header.TLabel").pack(side=tk.TOP,
                                                                                   anchor=tk.NW)
        ttk.Separator(self._topFrame, orient=tk.VERTICAL).pack(side=tk.LEFT, fill="y",
                                                               padx=20)
        ttk.Button(self._topFrame, text="Activate").place(x=40, y=100)
        ttk.Button(self._topFrame, text="+", command=self.addProfile).place(x=120, y=200)
        ttk.Button(self._topFrame, text="Refresh").place(x=40, y=200)
        ttk.Button(self._topFrame, text="Manual Input", command=self.textCommand).place(x=60, y=300)

        ttk.Label(self._topFrame, text="Ver 0.9.4", style="normal.TLabel").place(x=240, y=360)

        ttk.Button(self._topFrame, image=self._icon, command=self.openCredits).place(x=300, y=350)

    def start(self):
        self.test.start()
        self.addStyle()
        self.makeWidgets()
        self._root.mainloop()


test = medGui()
test.start()
