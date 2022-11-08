import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance converter")

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        frame = FeetToMeters(self)
        frame.grid(row=0, column=0, sticky="NSEW")

        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)


class MetersToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        
        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)

        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=0, sticky="EW")
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMeters(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Segoe UI", 15))
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)

        feet_label.grid(column=0, row=0, sticky="W")
        feet_input.grid(column=1, row=0, sticky="EW")
        feet_input.focus()

        meters_label.grid(column=0, row=1, sticky="W")
        meters_display.grid(column=1, row=1, sticky="EW")

        calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
    
    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f"{meters:.3f}")
        except ValueError:
            pass


if __name__ == "__main__":
    root = DistanceConverter()
    font.nametofont("TkDefaultFont").configure(size=15)
    root.columnconfigure(0, weight=1)
    root.mainloop()
 