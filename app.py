import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Distance converter")

meters_value = tk.StringVar()


def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet:.3f} feet.")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 50))
main.grid()

meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value)
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main , text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meters_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
meters_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
meters_input.focus()

feet_label.grid(column=0, row=1, stick="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)



if __name__ == "__main__":
    root.mainloop()
 