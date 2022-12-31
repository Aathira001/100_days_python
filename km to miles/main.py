import tkinter as tk


def convert_miles_to_km():
    miles_value = miles.get()
    km_value = int(miles_value) * 1.609
    km_output.config(text=f"{km_value}")


window = tk.Tk()
window.title("Miles to km Converter")
window.config(padx=10, pady=10)

miles = tk.Entry(width=15)
miles.grid(padx=10)
miles.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to ")
equal_label.grid(column=0, row=1)

km_output = tk.Label(text="0")
km_output.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

convert_button = tk.Button(text="Convert", command=convert_miles_to_km)
convert_button.grid(column=1, row=3)

window.mainloop()
