from tkinter import *


def km_to_miles():
    km = float(kmph_input.get())
    miles = round(km / 1.609)
    miles_result_label.config(text=f"{miles}")


window = Tk()
window.title("Kilometer to Miles Converter")
window.config(padx=20, pady=20)


kmph_input = Entry(width=5)
kmph_input.grid(column=1, row=0)


kmph_label = Label(text="Kilometer")
kmph_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)


miles_result_label = Label(text="0")
miles_result_label.grid(column=1, row=1)


miles_label = Label(text="Mi")
miles_label.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()
