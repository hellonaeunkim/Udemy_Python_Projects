from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km}")

#calls action() when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()