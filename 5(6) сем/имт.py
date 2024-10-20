from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value_1 = float(mass.get()) 
        value_2 = float(height.get()) 
        bmi_1 = ((value_1)/((value_2**2))) 
        bmi.set(int(bmi_1))  
        if bmi_1 <= 16:
            puk.set("Выраженный дефицит массы тела")
        if 16 < bmi_1 <= 18.5 : 
            puk.set("Недостаточная (дефицит) масса тела")
        if 18.5 < bmi_1 <= 25 :
            puk.set("Выраженный дефицит массы тела")
        if 25 < bmi_1 <= 30 :
            puk.set("Избыточная масса тела (предожирение)")
        if 30 < bmi_1 <= 35 :
            puk.set("Ожирение 1 степени")
        if 35 < bmi_1 < 40 :
            puk.set("Ожирение 2 степени")
        if bmi_1 >= 40:
            puk.set("Ожирение 3 степени")
    except ValueError:
        pass

    def interpretation(puk):
            if bmi_1 <= 16:
                puk.set("Выраженный дефицит массы тела")
            if 16 < bmi_1 <= 18.5 : 
                puk.set("Недостаточная (дефицит) масса тела")
            if 18.5 < bmi_1 <= 25 :
                puk.set("Выраженный дефицит массы тела")
            if 25 < bmi_1 <= 30 :
                puk.set("Избыточная масса тела (предожирение)")
            if 30 < bmi_1 <= 35 :
                puk.set("Ожирение 1 степени")
            if 35 < bmi_1 < 40 :
                puk.set("Ожирение 2 степени")
            if bmi_1 >= 40:
                puk.set("Ожирение 3 степени")



root = Tk()
root.title("bmi")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=2, sticky=(W, E))

bmi = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=2, row=3, sticky=(W, E))

puk = StringVar()
ttk.Label(mainframe, textvariable=puk).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=4, sticky=W)

ttk.Label(mainframe, text="масса, кг").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="рост, м").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="индекс массы тела:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


mass_entry.focus()

root.bind("<Return>", calculate)

root.mainloop()