from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Firewall Module")

headerFont = ("Helvetica", 16, "bold")

root.geometry("650x350")

rightFrame = Frame(root, width=300, height=300, bd=3, padx=30, relief=RIDGE)
rightFrame.pack(side=RIGHT, expand=1, fill=Y)

leftFrame = Frame(root, width=300, height=300, bd=3, relief=RIDGE)
leftFrame.pack(side=LEFT, expand=1, fill=Y)

headerLeft = Label(leftFrame, text="INFO WINDOW", font=headerFont)
headerLeft.grid(row=0, column=0, pady=20)

messageFrame = Frame(leftFrame, width=300, height=250, bd=3, bg="#ffffb3", relief=SUNKEN)
messageFrame.grid(row=1, column=0, sticky=E, padx=30)
messageFrame.columnconfigure(0, weight=1)


headerRight = Label(rightFrame, text="SETTINGS WINDOW", font=headerFont)
headerRight.grid(row=0, column=0, columnspan=3, pady=20)

sketchTypeLabel = Label(rightFrame, text="Sketch Type: ")
sketchTypeLabel.grid(row=1, column=0, sticky=W)
sketchType = ttk.Combobox(rightFrame, values=("a", "b", "c"), state="readonly")
sketchType.grid(row=1, column=1, columnspan=2)

TimeIntervalLabel = Label(rightFrame, text="Time Interval: ")
TimeIntervalLabel.grid(row=2, column=0, sticky=W)
TimeInterval = ttk.Combobox(rightFrame, values=("0.25", "0.50", "0.75"), state="readonly")
TimeInterval.grid(row=2, column=1, pady=10, columnspan=2)
TimeInterval.set("0.25")

TimeIntervalLabel = Label(rightFrame, text="Hash Type: ")
TimeIntervalLabel.grid(row=3, column=0, sticky=W)
TimeInterval = ttk.Combobox(rightFrame, values=("hash1", "hash2", "hash3"), state="readonly")
TimeInterval.grid(row=3, column=1, columnspan=2)

var1 = IntVar()
TimeIntervalLabel = Label(rightFrame, text="Prevention: ")
TimeIntervalLabel.grid(row=4, column=0, sticky=W, pady=10)
R1 = Radiobutton(rightFrame, text="Enabled", variable=var1, value=1)
R1.grid(row=4, column=1)
R1.select()
R2 = Radiobutton(rightFrame, text="Disabled", variable=var1, value=2)
R2.grid(row=4, column=2)

var2 = IntVar()
TimeIntervalLabel = Label(rightFrame, text="Logging: ")
TimeIntervalLabel.grid(row=5, column=0, sticky=W)
R3 = Radiobutton(rightFrame, text="Enabled", variable=var2, value=1)
R3.grid(row=5, column=1)
R3.select()
R4 = Radiobutton(rightFrame, text="Disabled", variable=var2, value=2)
R4.grid(row=5, column=2)

saveButton = Button(rightFrame, text="SAVE", width=20, bg="#b3b3b3")
saveButton.grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()
