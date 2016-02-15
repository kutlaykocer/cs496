from tkinter import *
from tkinter import ttk

class GUI:
    radioButtonVar1 = None
    radioButtonVar2 = None
    sketchType      = None
    timeInterval    = None
    hashType        = None

    def pressedSaveButton(self):
        print(self.sketchType.get())
        print(self.timeInterval.get())
        print(self.hashType.get())
        print(self.radioButtonVar1.get())
        print(self.radioButtonVar2.get())

    def __init__(self):
        
        root = Tk()
        root.title("Firewall Module")
        headerFont = ("Helvetica", 16, "bold")
        s=ttk.Style()
        s.theme_use('clam')
        root.geometry("650x350")

        rightFrame = Frame(root, width=300, height=300, bd=3, padx=30, relief=RIDGE)
        rightFrame.pack(side=RIGHT, expand=1, fill=Y)

        leftFrame = Frame(root, width=300, height=300, bd=3, relief=RIDGE)
        leftFrame.pack(side=LEFT, expand=1, fill=Y)
        #Left Side Components BEGIN
        headerLeft = Label(leftFrame, text="INFO WINDOW", font=headerFont)
        headerLeft.grid(row=0, column=0, pady=20)

        messageFrame = Frame(leftFrame, width=300, height=250, bd=3, bg="#ffffb3", relief=SUNKEN)
        messageFrame.grid(row=1, column=0, sticky=E, padx=30)
        messageFrame.columnconfigure(0, weight=1)
        #Left Side Components END

        #Right Side Components BEGIN
        headerRight = Label(rightFrame, text="SETTINGS WINDOW", font=headerFont)
        headerRight.grid(row=0, column=0, columnspan=3, pady=20)

        sketchTypeLabel = Label(rightFrame, text="Sketch Type: ")
        sketchTypeLabel.grid(row=1, column=0, sticky=W)
        self.sketchType = ttk.Combobox(rightFrame, values=("One-Dimensional", "Multi Dimensional"), state="readonly")
        self.sketchType.grid(row=1, column=1, columnspan=2)
        self.sketchType.current(0)

        timeIntervalLabel = Label(rightFrame, text="Time Interval: ")
        timeIntervalLabel.grid(row=2, column=0, sticky=W)
        self.timeInterval = ttk.Combobox(rightFrame, values=("0.25", "0.50", "0.75"), state="readonly")
        self.timeInterval.grid(row=2, column=1, pady=10, columnspan=2)
        self.timeInterval.current(0)

        hashTypeLabel = Label(rightFrame, text="Hash Type: ")
        hashTypeLabel.grid(row=3, column=0, sticky=W)
        self.hashType = ttk.Combobox(rightFrame, values=("hash1", "hash2", "hash3"), state="readonly")
        self.hashType.grid(row=3, column=1, columnspan=2)
        self.hashType.current(0)

        self.radioButtonVar1 = IntVar()
        preventionLabel = Label(rightFrame, text="Prevention: ")
        preventionLabel.grid(row=4, column=0, sticky=W, pady=10)
        R1 = Radiobutton(rightFrame, text="Enabled", variable=self.radioButtonVar1, value=1)
        R1.grid(row=4, column=1)
        R1.select()
        R2 = Radiobutton(rightFrame, text="Disabled", variable=self.radioButtonVar1, value=2)
        R2.grid(row=4, column=2)

        self.radioButtonVar2= IntVar()
        loggingLabel = Label(rightFrame, text="Logging: ")
        loggingLabel.grid(row=5, column=0, sticky=W)
        R3 = Radiobutton(rightFrame, text="Enabled", variable=self.radioButtonVar2, value=1)
        R3.grid(row=5, column=1)
        R3.select()
        R4 = Radiobutton(rightFrame, text="Disabled", variable=self.radioButtonVar2, value=2)
        R4.grid(row=5, column=2)

        saveButton = Button(rightFrame, text="SAVE", width=20, bg="#b3b3b3", command = self.pressedSaveButton)
        saveButton.grid(row=6, column=0, columnspan=3, pady=20)
        #Right Side Components END
        root.mainloop()
        

    

app = GUI()
